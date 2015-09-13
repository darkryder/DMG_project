library(FSelector)
library(rpart)
table <- read.csv("numeric_train.csv", header=0);
    table <- na.omit(v[,colSums(is.na(table))<nrow(table)])
    #print (table)
    nms <- colnames(table)
    model <- information.gain(as.formula(paste(nms[length(nms)],"~.")), table)
    print (model)
    for (i in 1:length(nms)){
    write.csv(model[[i]],'gain.csv')}
    #model<-rpart(as.formula(paste(nms[length(nms)],"~.")),data=table)
    #print (summary(model))

