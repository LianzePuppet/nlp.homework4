# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 23:07
# @Author  : Deng Qidong
# @FileName: get_abstract.py
# @Software: PyCharm


def find_dot(add,str_list:str,char_1:str):
    count = add
    list1=list()
    for each_char in str_list:
        count += 1
        if each_char == char_1:
            #print(each_char, count - 1)
            list1.append(count)
    return list1




species_set=set()
with open ('./data/result.txt','r',encoding="utf-8")as f1:
    count=0#统计count数目
    with open('./data/Chemical_interaction.sif','w',encoding='utf-8') as f2:
        for line in f1:
            if line !='\n':
                line = line.strip().split('\t')#如果分成6部分说明是标注行，1则是标题或者摘要
                if len(line)==1:
                    line=str(line[0]).split('|')
                    if line[1]=='t':
                        title_len=len(line[2])#标题的长度，一般标题都是一句话
                        l=line[2].split('.')
                        dot_index.append(title_len-1)#得到标题的句号Index
                    elif line[1]=='a':
                        abstract=line[2]
                        dot_index=dot_index + find_dot(title_len, line[2],".")
                        dot_index=dot_index + find_dot(title_len, line[2], "!")
                        dot_index=dot_index + find_dot(title_len, line[2], "?")
                        #这样我们就得到了标点的位置列表dot_index
                else:
                    new_article=new_article+1
                    if new_article==1:
                    #也就是我们真正的实体行了
                        a=int(line[1]);b=int(line[2]);word1=line[3];type1=line[4]
                    else:
                        c=int(line[1]);d=int(line[2]);word2=line[3];type2=line[4]
                        for i in range(len(dot_index)-1):
                            if a>dot_index[i] and b<dot_index[i+1] and c>dot_index[i] and d<dot_index[i+1] and word1!=word2:
                                if type1 == "Chemical" and type2 == "Chemical":
                                    f2.write(word1 + "\tChemical-Chemical\t" + word2 + "\n")
                                if (type1=="Chemical" and type2=="Species")or(type1=="Species" and type2=="Chemical"):
                                    f2.write(word1 + "\tChemical-species\t" + word2 + "\n")
                                if (type1 == "Gene" and type2 == "Chemical") or (type1 == "Chemical" and type2 == "Gene"):
                                    f2.write(word1 + "\tchemical-gene\t" + word2 + "\n")
                            if type1=="Chemical":
                                species_set.add(word1)
                            if type2 == "Chemical":
                                species_set.add(word2)
                            a=c;b=d;word1=word2;type1=type2
            else:#也就是到了下一篇文献了
                count = count + 1#记录文献总数
                dot_index=list()#标点信息重置
                new_article=0
with open ('./data/Chemical_set.txt','w',encoding='utf-8') as f3:
    for i in species_set:
         f3.write(i+"\ti\n")
    f3.close()
