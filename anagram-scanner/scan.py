
import sys

def is_anagram(a,b):
    if len(a) != len(b):
       return "bukan anagram"

    t1,t2 = sorted(a),sorted(b)

    if t1 != t2:
       return "bukan anagram"
    return "Yap ini adalah anagram"


if __name__=="__main__":
   print (is_anagram(sys.argv[1],sys.argv[2]))
