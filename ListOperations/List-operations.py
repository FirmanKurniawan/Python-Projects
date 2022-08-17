import math

class Liste():
    def __init__(self):
        self.list_1 = []
        
    def append_to_list(self,append_sth):
        self.append = append_sth
        self.list_1.append(self.append)

    def insert_to_list(self,inserted_number,number_index):
        self.inserted_number = inserted_number
        self.number_index = number_index
        self.list_1.insert(self.inserted_number,self.number_index)
    
    def remove_from_list(self,remove_first_element):
        self.remove_first_element = remove_first_element
        self.list_1.remove(self.remove_first_element)
            
    def sort_the_list(self):
        self.list_1 = sorted(self.list_1)
        
    def pop_last_element(self):
        self.list_1.pop(-1)

    def reverse_the_list(self):
        self.list_1.reverse()

    def return_result(self):
        return self.list_1

    def print_the_list(self):
        print(self.list_1)


if __name__ == '__main__':
    N = int(input())
    obj = Liste()
    final_result= []
    for i in range(N):
        multiple_inputs = input().rstrip().split(" ")

        if multiple_inputs[0] == "append":
            obj.append_to_list(int(multiple_inputs[1]))
        elif multiple_inputs[0] == "insert":
            obj.insert_to_list(int(multiple_inputs[1]),int(multiple_inputs[2]))
        elif multiple_inputs[0] == "remove":
            obj.remove_from_list(int(multiple_inputs[1]))
        elif multiple_inputs[0] == "sort":
            obj.sort_the_list()     
        elif multiple_inputs[0] == "pop":
            obj.pop_last_element()  
        elif multiple_inputs[0] == "reverse":
            obj.reverse_the_list()    
        elif multiple_inputs[0] == "print":
            obj.print_the_list()                                                      
    # result_as_str = obj.return_result()

    # for number in result_as_str:
    #     number = int(number)
    #     final_result.append(number)
    
    #print(final_result)

