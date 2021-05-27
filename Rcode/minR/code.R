library(pubmed.mineR)
pubmed_abstracts <- readabs("E:/Desktop/NLP/作业4/Rcode/abstract-rice-set.txt")
pmid <-  pubmed_abstracts@PMID#得到pmid
pubmed_abstracts
p53_words <- word_atomizations(pubmed_abstracts)
