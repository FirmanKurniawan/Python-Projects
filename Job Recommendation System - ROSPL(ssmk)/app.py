import streamlit as st
import pickle
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity

pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)  

def predict(text):
    data = pd.read_csv("dataset.csv")
    data = data.drop(["Crawl Timestamp", "Uniq Id", "Location", "Role", "Job Salary"], axis="columns")
    data.dropna(inplace=True)
    lst1 = []

    # Preprocess the data
    for i in data["Key Skills"]:
        x = i.split("|")
        lst1.append(x)
    data["KeySkills"] = lst1
    data = data.drop(["Key Skills"], axis="columns")

    def list_to_string(lst):
        return ', '.join(lst)

    data['KeySkills'] = data['KeySkills'].apply(list_to_string)
    job = []
    stopwordslist = []
    cleanjobs = []

    # Read stopwords
    with open("stopwords.txt", "r", encoding="utf-8") as f:
        for word in f:
            word = word.split('\n')
            stopwordslist.append(word[0])

    # Preprocess job titles
    for i in data["Job Title"]:
        jobs = i.lower()
        job.append(jobs)
    for j in job:
        text_tokens = word_tokenize(j)
        tokens_without_sw = [f for f in text_tokens if not f in stopwordslist]
        cleanjobs.append(' '.join(tokens_without_sw))
    data["clean_JobTitle"] = cleanjobs
    skillsTokenized = []
    stopwordsSkills = []

    # Read stopwords for skills
    with open("stopwords.txt", "r", encoding="utf-8") as f:
        for word in f:
            word.lower()
            word = word.split('\n')
            stopwordsSkills.append(word[0])

    # Tokenize and preprocess skills
    for k in data["KeySkills"].values:
        k = str(k).split(', ')
        skillstokens_without_sw = [f for f in k if not f.lower() in stopwordsSkills]
        for j in skillstokens_without_sw:
            skillsTokenized.append(j)

    df = pd.DataFrame({'skills': skillsTokenized})
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data["clean_JobTitle"].values)

    analyze = vectorizer.build_analyzer()
    wcss = []

    for i in range(1, 15):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, max_iter=600, n_init=1)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    true_k = 7
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=600, n_init=1, random_state=42)
    pred = model.fit_predict(X)
    sklearn_pca = PCA(n_components=2)
    Y_sklearn = sklearn_pca.fit_transform(X.toarray())

    kmeans = KMeans(n_clusters=7, init='k-means++', max_iter=600, n_init=1, random_state=42)
    label = []

    for i in data["clean_JobTitle"].values:
        vec = vectorizer.transform([i])
        pred = model.predict(vec)
        if pred == 0:
            label.append("Software Engineer")
        elif pred == 1:
            label.append("HR")
        elif pred == 2:
            label.append("Marketing / Sales Executive")
        elif pred == 3:
            label.append("Backend Developer")
        elif pred == 4:
            label.append("Business Solution Consultant")
        elif pred == 5:
            label.append("Analyst")
        else:
            label.append("IT Business Management")

    data['Label'] = label
    jobSkills = []

    for i in data["KeySkills"]:
        jobSkills.append(i.lower())

    Xclass = vectorizer.fit_transform(jobSkills)
    X_train, X_test, Y_train, Y_text = train_test_split(Xclass, label, test_size=0.2, random_state=42)
    c_value = 1.0
    lrg = LogisticRegression(penalty='l2', C=c_value, random_state=42)
    lrg.fit(X_train, Y_train)

    pred = vectorizer.transform([text.lower()])
    output = lrg.predict(pred)
    
    result = "You may look into " + output[0] + " jobs : "
    
    # Additional processing for job recommendations
    cos = []
    labelData = data[data["Label"] == output[0]]
    
    for index, row in labelData.iterrows():
        skills = [row["KeySkills"]]
        skillVec = vectorizer.transform(skills)
        cos_lib = cosine_similarity(skillVec, pred)
        cos.append(cos_lib[0][0])
    
    labelData["Cosine_similarity"] = cos
    top_5 = labelData.sort_values('Cosine_similarity', ascending=False)[['Job Title', 'Job Experience Required', 'Role Category', 'Functional Area', 'Industry', 'KeySkills']]
    

    return result, top_5

    

st.title("Job Recommendation System")

text = st.text_input("Please enter your skills below: ")
# st.button("Submit")
if st.button('Predict'):
    # Make predictions using the loaded model
    # print("Debug - Value of 'a':", a)
    # print(type(text))
    # output = predict(text)
    # st.write(output)
    if text:
        result, top_5 = predict(text)

        # Display the general recommendation
        st.write(result)

        # Display the job recommendations in a table format
        st.dataframe(top_5)

    else:
        st.warning("Please enter your skills before predicting.")
