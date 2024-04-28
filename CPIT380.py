from jes4py import *
#1 ========================================================================================================================================
def reflect_horizontal_1():
    file = pickAFile()
    source = makePicture(file)
    mirrorPoint = getWidth(source) / 2
    width = getWidth(source)
    for y in range(0,getHeight(source)):
        for x in range(0,(int)(mirrorPoint)):
            leftPixel = getPixel(source,x,y)
            rightPixel = getPixel(source,width - x - 1,y)
            color = getColor(leftPixel)
            setColor(rightPixel,color)
    explore(source)

def reflect_vertical_1():
    file = pickAFile()
    source = makePicture(file)
    mirrorPoint = getHeight(source) / 2
    height = getHeight(source)
    for x in range(0,getWidth(source)):
        for y in range(0,(int)(mirrorPoint)):
            topPixel = getPixel(source,x,height - y - 1)
            bottomPixel = getPixel(source,x,y) 
            color = getColor(bottomPixel)
            setColor(topPixel,color)
    explore(source)

def reflect_horizontal_2():
    file = pickAFile()
    source = makePicture(file)
    mirrorPoint = getWidth(source) / 2
    width = getWidth(source)
    for y in range(0,getHeight(source)):
        for x in range(0,(int)(mirrorPoint)):
            leftPixel = getPixel(source,width - x - 1,y)
            rightPixel = getPixel(source,x,y)
            color = getColor(leftPixel)
            setColor(rightPixel,color)
    explore(source)

def reflect_vertical_2():
    file = pickAFile()
    source = makePicture(file)
    mirrorPoint = getHeight(source) / 2
    height = getHeight(source)
    for x in range(0,getWidth(source)):
        for y in range(0,(int)(mirrorPoint)):
            topPixel = getPixel(source,x,y)
            bottomPixel = getPixel(source,x,height - y - 1) 
            color = getColor(bottomPixel)
            setColor(topPixel,color)
    explore(source)



#left to right
def reflect_diagonal_v1_d1():
    file = pickAFile()
    source = makePicture(file)
    width = getWidth(source) 
    hight = getHeight(source) 
    canvas = makeEmptyPicture(width,hight)
    targetX = 0
    for sourceX in range(0,getWidth(source)): 
        targetY = 0 
        sourceY = 0
        for sourceY in range(0,getHeight(source)): 
            srcpix = getPixel(source,sourceX,sourceY) #give me the coordnate of x and y for this pixel then get it's color 
            color = getColor(srcpix)
            if(sourceX> sourceY): #check if the the source x is bigger than source y to know if it's in the upper or not
                if(sourceY >= hight or sourceX >= width or sourceY>= width or sourceX >= hight):
                    break
                targetpix=getPixel(canvas, sourceY, sourceX) #if it's in the upper than swap them
                setColor(targetpix, color)
                setColor(getPixel(canvas, sourceX, sourceY),color)
            elif(sourceX==sourceY): #to draw the middle line 
                targetpix=getPixel(canvas, sourceY, sourceX) 
                setColor(getPixel(canvas, sourceX, sourceY),color)
    explore(canvas)



#right to left
def reflect_diagonal_v1_d2():
    file = pickAFile()
    source = makePicture(file)
    width = getWidth(source) 
    hight = getHeight(source) 
    canvas = makeEmptyPicture(width,hight)
    targetX = 0
    for sourceX in range(0,getWidth(source)): 
        targetY = 0 
        sourceY = 0
        for sourceY in range(0,getHeight(source)): 
            srcpix = getPixel(source,sourceX,sourceY) #give me the coordnate of x and y for this pixel then get it's color 
            color = getColor(srcpix)
            if(sourceX< sourceY): #check if the the source x is bigger than source y to know if it's in the upper or not
                if(sourceY >= hight or sourceX >= width or sourceY>= width or sourceX >= hight): #this if statment to check if we go out of the image range
                    break
                targetpix=getPixel(canvas, sourceY, sourceX) #if it's in the lower than swap them
                setColor(targetpix, color)
                setColor(getPixel(canvas, sourceX, sourceY),color)
            elif(sourceX==sourceY): #to draw the middle line 
                targetpix=getPixel(canvas, sourceY, sourceX) 
                setColor(getPixel(canvas, sourceX, sourceY),color)
    explore(canvas)



#lower to upper 
def reflect_diagonal_v2_d1():
    file = pickAFile()
    source = makePicture(file)
    width = getWidth(source) 
    hight = getHeight(source) 
    if(width !=hight): #only works of the size is fixed !
        return -1
    for sourceX in range(0,width):
        for sourceY in range(0,width-sourceX):
            pixS= getPixel(source,width-sourceX-1,width-sourceY-1)
            color = getColor(pixS)
            pixT= getPixel(source,sourceY,sourceX)
            setColor(pixT,color)
    explore(source)



#upper to lower
def reflect_diagonal_v2_d2():
    file = pickAFile()
    source = makePicture(file)
    width = getWidth(source) 
    hight = getHeight(source) 
    if(width !=hight): #only works of the size is fixed !
        return -1
    for sourceX in range(0,width):
        for sourceY in range(0,width-sourceX):
            pixS= getPixel(source,sourceY,sourceX)
            color = getColor(pixS)
            pixT= getPixel(source,width-sourceX-1,width-sourceY-1) 
            setColor(pixT,color)
    explore(source)



def rotate_left():
    file = pickAFile()
    source = makePicture(file)
    width = getWidth(source) 
    hight = getHeight(source) 
    canvas = makeEmptyPicture(width,hight)
    targetX = 0
    for sourceX in range(0,width):
        targetY = 0
        for sourceY in range(0,hight):
            if(width !=hight): #only works of the size is fixed !
                return -1
            srcpix = getPixel(source,sourceX,sourceY)
            color = getColor(srcpix)         
            targetpix=getPixel(canvas, hight-sourceY-1 , sourceX) #the change is here check it out !
            setColor(targetpix, color)
            targetY = targetY + 1
            targetX = targetX + 1
    explore(canvas)



def rotate_right():
    file = pickAFile()
    source = makePicture(file)
    width = getWidth(source) 
    hight = getHeight(source) 
    canvas = makeEmptyPicture(width,hight)
    targetX = 0
    for sourceX in range(0,width):
        targetY = 0
        for sourceY in range(0,hight):
            if(width !=hight): #only works of the size is fixed !
                return -1
            srcpix = getPixel(source,sourceX,sourceY)
            color = getColor(srcpix)
	 	#Change is here                
            targetpix=getPixel(canvas, sourceY , width-sourceX-1) #the change is here check it out !
            setColor(targetpix, color)
            targetY = targetY + 1
            targetX = targetX + 1
    explore(canvas)

#1 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#2 ========================================================================================================================================
def smaller(src,num):
    width = getWidth(src) 
    hight = getHeight(src) 
    canvas = makeEmptyPicture(int(width/(num)),int(hight/(num)))
    sourceX = 0
    for targetX in range(0,int(width/(num))):
        sourceY = 0
        for targetY in range(0,int(hight/(num))):
            color = getColor(getPixel(src,sourceX,sourceY))
            setColor(getPixel(canvas,targetX,targetY), color)
            sourceY = sourceY + (num)
        sourceX = sourceX + (num)
    explore(canvas)

def bigger(src,num):
    width = (getWidth(src) )
    hight = (getHeight(src)  )
    canvas = makeEmptyPicture(width*num,hight*num)
    sourceX = 0
    for targetX in range(0,width*num):
        sourceY = 0
        for targetY in range(0,hight*num):
            color = getColor(getPixel(src,int(sourceX),int(sourceY)))
            setColor(getPixel(canvas,targetX,targetY), color)
            sourceY = sourceY +(1/num)
        sourceX = sourceX + (1/num)
    explore(canvas)

def smallerPer(src,per):
    width = getWidth(src) 
    hight = getHeight(src) 
    per = per *0.01
    per = 1- per
    canvas = makeEmptyPicture(int(width*per),int(hight*per))
    sourceX = 0
    for targetX in range(0,int(width*per)):
        sourceY = 0
        for targetY in range(0,int(hight*per)):
            color = getColor(getPixel(src,sourceX,sourceY))
            setColor(getPixel(canvas,targetX,targetY), color)
            sourceY = sourceY + (1/per)
        sourceX = sourceX + (1/per)
    explore(canvas)

def biggerPer(src,per):
    width = getWidth(src) 
    hight = getHeight(src)
    per =  100+per #to not scale down the image
    per = per *0.01 #convert it into persntage
    canvas = makeEmptyPicture(int(width*per),int(hight*per))
    sourceX = 0
    for targetX in range(0,int(width*per)):
        sourceY = 0
        for targetY in range(0,int(hight*per)):
            color = getColor(getPixel(src,int(sourceX),int(sourceY)))
            setColor(getPixel(canvas,targetX,targetY), color)
            sourceY = sourceY + (1/per)
        sourceX = sourceX + (1/per)
    explore(canvas)

#2 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#3 ========================================================================================================================================


#3 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



#4 ========================================================================================================================================


#4 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||