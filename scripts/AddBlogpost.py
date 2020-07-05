from datetime import datetime
timeStamp = datetime.now().strftime("%B %d, %Y, %H:%M") #Time stamps
blogDIR="../blog.html"  #html DIR
cssDIR="../css/hiddencontent.css"   #css DIR
jsDIR="hidden.js"   #js DIR

BlogTitle = input("Enter BlogTitle:")   #Get unique blog title for divs and well the blog title...
BlogCode = BlogTitle.replace(" ", "") #Make the unique div id the blog title with no whitespace 



#write the blog template to blog.html file.
def writeToHTML():
    f = open("../blog.html", "r")
    contents = f.readlines()    #getting ready to insert in specific line
    f.close()

    contents.insert(90, 
    """

<div id="hidden-content">
    <div class="click"""+BlogCode+"""">
        <h1>"""+BlogTitle+"""</h1>
        <h3>"""+timeStamp+"""</h3>
    </div>

    <div class="expand"""+BlogCode+"""">
        <p>
            
        </p>
    </div>
</div>
<hr>

    """)

    f = open(blogDIR, "w")   #Getting ready to rewrite with the appended text
    contents= "".join(contents) 
    f.write(contents)
    f.close()




#only need to append at end of css file, no need to store all lines and rewrite
def writeToCSS():
    f = open(cssDIR, "a") 
    f.write(
        """

#hidden-content div.expand"""+BlogCode+"""{
display:none;
margin-top:0px;
padding: 10px 20px 20px 20px;
z-index:-4;
}

        """)
    f.close()





#only need to append at end of js file, no need to store all lines and rewrite
def writeToJS():
    f=open(jsDIR, "a")
    f.write(
        """

$(".click"""+BlogCode+"""").click(function(){
$(".expand"""+BlogCode+"""").slideToggle();
});
    
    """)





writeToHTML() #write to hmtl file
writeToCSS()  #write to css file
writeToJS()   #write to js file