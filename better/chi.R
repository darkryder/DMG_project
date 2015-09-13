# we can make a new csv file for categorical attribute to
########make a list gg=[] having var names(eg 1,5,6,) which are
#CATEGORICAl then run a loop for i in gg:do// else continue, same for j
v<-read.csv('cleaned_train_small.csv',header=T)
#i<-100#taking into account ID but should be 2
data<-paste(c('chisquare','i','j'),collapse=",")
write(data,'chi.csv',append=T)
flag=0

printable_index <- function(i){
    answer = i
    if (i <= 218) {
        answer = i-1
    }
    if (i >= 240) {
        answer = i+1
    }
    return (i)
}

read<-read.csv('attr.csv')[[1]]
len<-1

####no i loop reqd then


indexi = 1
indexj = 2

while(len<length(read))
{
    i<-printable_index(read[[len]])

    len1<-len+1
    print("i:")
    print(i)
    print("\n")
    while(len1<=length(read)) #1933
    {
    j<-printable_index(read[[len1]])
    d<-c(na.omit(v[[i]]),na.omit(v[[j]]))
    ### for(i in 1:length(d)){
        ### if(d[i]<0){d[i]<-NA}}
    chisq<-chisq.test(na.omit(table(d)))
    chi<-chisq[[1]]
     if(flag==0){
         min=chi
         flag=1
         indexi=i
         indexj=j
         }
    if(min>chi){
        min=chi
        indexi=i
        indexj=j
    }
    data<-paste(c(chi,printable_index(i),printable_index(j)),collapse=",")
    write(data,'chi.csv',append=T)
    len1<-len1+1
    }
    len<-len+1
}
print (min)
write('minimum','chi.csv',append=T, sep=",")
i=paste(c('VAR_',printable_index(indexi)),collapse="")
j=paste(c('VAR_',printable_index(indexj)),collapse="")
data<-paste(c(min,i,j),collapse=",")
write(data,'chi.csv',append=T, sep=",")