class Locker:
    def __init__(self):
        self.dictionary=dict()
        self.unlock_dictionary=dict()
        self.key="sP3h0yn0X2"
        count=0
        for i in range(33,127):
            self.dictionary[chr(i)]=count
            self.unlock_dictionary[count]=chr(i)
            count+=1
        for i in range(1040,1104):
            self.dictionary[chr(i)]=count
            self.unlock_dictionary[count]=chr(i)
            count+=1
        self.count=count
    def lock(self,word):
        key=self.key
        len_word=len(word)
        len_key=len(key)
        word_index=[]
        key_index=[]
        for i in range(len_word):
            word_index.append(self.dictionary[word[i]])
        for i in range(len_key):
            key_index.append(self.dictionary[key[i]])
        if len_word>len_key:
            add_len=len_word//len_key+1
            key_index*=add_len
        res_index=[]
        for i in range(len_word):
            test_index=word_index[i]+key_index[i]
            if test_index>=self.count:
                test_index=test_index-self.count
            res_index.append(test_index)
        lock_word=""
        for i in range(len_word):
            lock_word+=self.unlock_dictionary[res_index[i]]
        return lock_word

    def unlock(self,lock_word):
        key=self.key
        len_word=len(lock_word)
        len_key=len(key)
        word_index=[]
        key_index=[]
        for i in range(len_word):
            word_index.append(self.dictionary[lock_word[i]])
        for i in range(len_key):
            key_index.append(self.dictionary[key[i]])
        if len_word>len_key:
            add_len=len_word//len_key+1
            key_index*=add_len
        res_index=[]
        for i in range(len_word):
            test_index=word_index[i]-key_index[i]
            if test_index<0:
                test_index=self.count+test_index
            res_index.append(test_index)
        word=""
        for i in range(len_word):
            word+=self.unlock_dictionary[res_index[i]]
        return word
"""locker1=Locker()
text=input()
print("Исходный: ",text)
lock_text=locker1.lock(text)
print("Шифр: ",lock_text)
unlock_text=locker1.unlock(lock_text)
print("Расшифровка: ",unlock_text)"""
