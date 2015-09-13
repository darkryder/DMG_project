# we can make a new csv file for categorical attribute to
########make a list gg=[] having var names(eg 1,5,6,) which are CATEGORICAl then run a loop for i in gg:do// else continue, same for j
v<-read.csv('train_changepart.csv',header=T)
i<-215#taking into account ID but should be 2
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

while(i<=216)#1934 taking into account target, but should be 1933
{
    j<-i+1
    while(j<=216) #1933
    {
    print(j)
    d<-c(na.omit(v[[i]]),na.omit(v[[i+1]]))
    
    chi<-chisq.test(d)[[1]]
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
        
    
    print  (chi[[1]])
    
    
    
    data<-paste(c(chi,printable_index(i),printable_index(j)),collapse=",")
    write(data,'chi.csv',append=T)
    j<-j+1
    }
    i<-i+1
}


print (min)
write('minimum','chi.csv',append=T)
i=paste(c('VAR_',printable_index(indexi)),collapse="")
j=paste(c('VAR_',printable_index(indexj)),collapse="")
data<-paste(c(min,i,j),collapse=",")
write(data,'chi.csv',append=T)

