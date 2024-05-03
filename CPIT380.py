from jes4py import *
#1 ========================================================================================================================================
def reflect_horizontal_1(source):
    mirrorPoint = getWidth(source) / 2
    width = getWidth(source)
    for y in range(0,getHeight(source)):
        for x in range(0,(int)(mirrorPoint)):
            leftPixel = getPixel(source,x,y)
            rightPixel = getPixel(source,width - x - 1,y)
            color = getColor(leftPixel)
            setColor(rightPixel,color)
    return(source)

def reflect_vertical_1(source):
    mirrorPoint = getHeight(source) / 2
    height = getHeight(source)
    for x in range(0,getWidth(source)):
        for y in range(0,(int)(mirrorPoint)):
            topPixel = getPixel(source,x,height - y - 1)
            bottomPixel = getPixel(source,x,y) 
            color = getColor(bottomPixel)
            setColor(topPixel,color)
    return(source)

def reflect_horizontal_2(source):
    mirrorPoint = getWidth(source) / 2
    width = getWidth(source)
    for y in range(0,getHeight(source)):
        for x in range(0,(int)(mirrorPoint)):
            leftPixel = getPixel(source,width - x - 1,y)
            rightPixel = getPixel(source,x,y)
            color = getColor(leftPixel)
            setColor(rightPixel,color)
    return(source)

def reflect_vertical_2(source):
    mirrorPoint = getHeight(source) / 2
    height = getHeight(source)
    for x in range(0,getWidth(source)):
        for y in range(0,(int)(mirrorPoint)):
            topPixel = getPixel(source,x,y)
            bottomPixel = getPixel(source,x,height - y - 1) 
            color = getColor(bottomPixel)
            setColor(topPixel,color)
    return(source)



#left to right
def reflect_diagonal_v1_d1(source):
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
    return(canvas)



#right to left
def reflect_diagonal_v1_d2(source):
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
    return(canvas)



#lower to upper 
def reflect_diagonal_v2_d1(source):
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
    return(source)



#upper to lower
def reflect_diagonal_v2_d2(source):
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
    return(source)



def rotate_left(source):
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
    return(canvas)



def rotate_right(source):
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
    return(canvas)

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
    return(canvas)

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
    return(canvas)

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
    return(canvas)

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
    return(canvas)

#2 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#3 ========================================================================================================================================


#3 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



#4 ========================================================================================================================================


#4 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#5 ========================================================================================================================================

def luminance(pixel):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    return (r + g + b) / 3


def edgedetection_tlbr(source):
    for y in range(getHeight(source) - 1):
        for x in range(getWidth(source) - 1):
            topleft = getPixel(source, x, y)
            bottom_right = getPixel(source, x + 1, y + 1)
            top_left_lum = luminance(topleft)
            bottom_right_lum = luminance(bottom_right)
            tlC= makeColor(top_left_lum,top_left_lum,top_left_lum)
            brC = makeColor(bottom_right_lum,bottom_right_lum,bottom_right_lum)
            d=distance(tlC,brC)
            if (d > 10):
                setColor(topleft, black)
            else:
                setColor(topleft, white)
    addText(source,20,10,"THIS EDGE IS TOP-LEFT BUTTOM-RIGHT",acolor=makeColor(255,0,0))
    return(source)


def edge_detection_lr(source):
    for y in range(getHeight(source)):
        for x in range(getWidth(source) - 1):
            left = getPixel(source, x, y)
            right = getPixel(source, x + 1, y)
            left_lum = luminance(left)
            right_lum = luminance(right)
            leftC= makeColor(left_lum,left_lum,left_lum)
            rightC= makeColor(right_lum,right_lum,right_lum)
            d=distance(leftC,rightC)
            if (d > 10):
                setColor(left, black)
            else:
                setColor(left, white)
    addText(source,20,10,"THIS EDGE IS LEFT RIGHT",acolor=makeColor(255,0,0))
    return(source)


def edge_detection_tb(source):
    for x in range(getWidth(source)):
        for y in range(getHeight(source) - 1):
            top = getPixel(source, x, y)
            bottom = getPixel(source, x, y + 1)
            top_lum = luminance(top)
            bottom_lum = luminance(bottom)
            topC = makeColor(top_lum,top_lum,top_lum)
            botC = makeColor(bottom_lum,bottom_lum,bottom_lum)
            d=distance(botC,topC)
            if (d > 10):
                setColor(top, black)
            else:
                setColor(top, white)
    addText(source,20,10,"THIS EDGE IS TOP BUTTOM",acolor=makeColor(255,0,0))
    return(source)


def background(image,oldBackGround,newBackGround,t):
    for px in getPixels(image):
        x = getX(px)
        y = getY(px)
        bgPx = getPixel(oldBackGround,x,y)
        pxC = getColor(px)
        bgC = getColor(bgPx)
        d = distance(pxC,bgC)
        if (d<t):
            newC=getColor(getPixel(newBackGround,x,y))
            setColor(px,newC)
    return(image)


def foreground(image,oldBackGround,newBackGround,t):
    for px in getPixels(image):
        x = getX(px)
        y = getY(px)
        bgPx = getPixel(oldBackGround,x,y)
        pxC = getColor(px)
        bgC = getColor(bgPx)
        d = distance(pxC,bgC)
        if (d>t): #changes start from here ...
            newC=getColor(px) 
            target = getPixel(newBackGround,x,y)
            setColor(target,newC)
    return(newBackGround)

#5 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#6 ========================================================================================================================================


#6 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#7 ========================================================================================================================================

def CreateAudioCopyWithSpace(SourceAudio: Sound) -> Sound:
    #create a Copy of a Sound Object and adds some space after it, according to its sampling rate
    #This function expects a sound Object
    AudioCopy = makeEmptySound(getLength(SourceAudio) + int(0.1 * getSamplingRate(SourceAudio)))
    for SampleIndex in range(0,getLength(SourceAudio)):
        SampleValue = getSampleValueAt(SourceAudio,SampleIndex)
        setSampleValueAt(AudioCopy,SampleIndex,SampleValue)
    
    for SampleIndex in range(getLength(SourceAudio), getLength(AudioCopy)):
        setSampleValueAt(AudioCopy,SampleIndex,0)

    return AudioCopy

def copy(SourceAudio: Sound,Target: Sound,StartIndex):
    #this function will copy the source audio , into the target audio , starting at the given index
    Target_index = StartIndex
    for SampleIndex in range(0,getLength(SourceAudio)):
        #for each sample in the audio that we want to put in the target
        SampleValue = getSampleValueAt(SourceAudio,SampleIndex)
        setSampleValueAt(Target,Target_index,SampleValue)
        Target_index+=1

def increaseVolume(Sound):
    for sample in getSamples(Sound):
        value = getSampleValue(sample)
        setSampleValue(sample,value*4)
    return(Sound)

def SpliceSounds(Sound1: Sound,Sound2: Sound,increaseVolumeSet: bool = False) -> Sound:
    Sound1= CreateAudioCopyWithSpace(Sound1)
    Sound2= CreateAudioCopyWithSpace(Sound2)
    NewSound = makeEmptySound(getLength(Sound1) + getLength(Sound2))
    copy(Sound1,NewSound,0)
    copy(Sound2,NewSound,getLength(Sound1))
    NewSound=increaseVolume(NewSound)
    if(increaseVolumeSet==True):
        NewSound=increaseVolume(NewSound)
    return NewSound

def CreateAudioCopy(SourceAudio: Sound) -> Sound:
    #create a Copy of a Sound Object and returns it
    #This function expects a sound Object
    AudioCopy = makeEmptySound(getLength(SourceAudio))

    for SampleIndex in range(0,getLength(SourceAudio)):
        SampleValue = getSampleValueAt(SourceAudio,SampleIndex)
        setSampleValueAt(AudioCopy,SampleIndex,SampleValue)
    
    return AudioCopy

def simpleAvrgFilter(sound_for_filter,filterSize):
    offset = filterSize//2
    edited_sound= CreateAudioCopy(sound_for_filter)
    for i in range(offset,getLength(sound_for_filter) -offset):
        sum=0
        for k in range(-offset,offset+1):
            val= getSampleValueAt(sound_for_filter,i+k) / filterSize
            sum=sum+val
        setSampleValueAt(edited_sound,i,sum)
    sound_for_filter=edited_sound
    return sound_for_filter

def minFilter(sound_for_filter,filterSize):
    offset = filterSize//2
    edited_sound= CreateAudioCopy(sound_for_filter)
    for i in range(offset,getLength(sound_for_filter) -offset):
        min=99999999999 #reseting the min value
        for k in range(-offset,offset+1):
            val= getSampleValueAt(sound_for_filter,i+k)
            if(val<min):
                min=val
        setSampleValueAt(edited_sound,i,min)
    sound_for_filter=edited_sound
    return sound_for_filter

def maxFilter(sound_for_filter,filterSize):
    offset = filterSize//2
    edited_sound= CreateAudioCopy(sound_for_filter)
    for i in range(offset,getLength(sound_for_filter) -offset):
        max=0 #reseting the max value
        for k in range(-offset,offset+1):
            val= getSampleValueAt(sound_for_filter,i+k)
            if(val>max):
                max=val
        setSampleValueAt(edited_sound,i,max)
    sound_for_filter=edited_sound
    return sound_for_filter

def weightedFilter_3x3(sound_for_filter,index1,index2,index3):
    list=[]
    total=0
    total=index1+index2+index3
    if (total>1): #if the value is invlid show error message and end the filter 
        print("ERROR","Please make sure the total number doesn't Exceed 1")
        return -1
    list.append(index1)
    list.append(index2)
    list.append(index3)
    offset = 3//2
    edited_sound= CreateAudioCopy(sound_for_filter)
    for i in range(offset,getLength(sound_for_filter) -offset):
        sum=0
        weight=0
        for k in range(-offset,offset+1):
            val= getSampleValueAt(sound_for_filter,i+k) * list[weight] 
            sum=sum+val
            weight= weight+1
        setSampleValueAt(edited_sound,i,sum)
    sound_for_filter=edited_sound
    return sound_for_filter

#7 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


