v<-read.csv('cleaned_train.csv',header=T)

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
########make a list gg=[] having var names(eg 1,5,6,) which are CATEGORICAl then check if( i in gg) :do//// else i++
#i<-190
read<-read.csv('attr.csv')[[1]]
len<-1

####no i loop reqd then

while(len<=length(read))
{
    i<-printable_index(read[[len]])
    j<-1934# should be target 1934
    
    d<-c(na.omit(v[[i]]),na.omit(v[[j]]))

    chi<-chisq.test(d)[[1]]
    print(i)
    print  (chi[[1]])
    data<-paste(c(chi,printable_index(i),printable_index(j)),collapse=",")
    write(data,'chiq7.csv',append=T)
    
    len<-len+1
}
