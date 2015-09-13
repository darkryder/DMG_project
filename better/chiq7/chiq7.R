v<-read.csv('train_change.csv',header=T)

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
i<-1
while(i<=4)#1933 as 1934 is target
{
    j<-910# should be target 1934
    
    d<-c(na.omit(v[[i]]),na.omit(v[[i+1]]))

    chi<-chisq.test(d)[[1]]
    print(i)
    print  (chi[[1]])
    data<-paste(c(chi,printable_index(i),printable_index(j)),collapse=",")
    write(data,'chiq7.csv',append=T)
    
    i<-i+1
}
