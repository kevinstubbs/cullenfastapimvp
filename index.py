# this script is used to populate a word document template with data
import datetime as dt
from docx2pdf import convert
from docxtpl import DocxTemplate, InlineImage

doc = DocxTemplate("photoExhibitionTemplate2.docx")

# simulating data that I imagine would be received from Egnyte API in the future
processedImages = [
    {'image' :  InlineImage(doc, 'images/img1.jpg'), 'caption': 'I think this is a cat, the breed is: ___'},
    {'image' : InlineImage(doc, 'images/img2.jpg'), 'caption': 'I think this is a dog, the breed is: ___'},
    {'image' : InlineImage(doc,'images/img3.jpg'), 'caption': 'I think this is a puppy, the breed is: ___'} ]


# I will later figure out how to control image size
# processedImages = [
#     {'image' :  InlineImage(doc, 'images/catTest.jpg'), 'caption': 'I think this is a cat, the breed is: ___'},
#     {'image' : InlineImage(doc, 'images/dogTest.jpg'), 'caption': 'I think this is a dog, the breed is: ___'},
#     {'image' : InlineImage(doc,'images/dogTest2.jpg'), 'caption': 'I think this is a puppy, the breed is: ___'}, 
#     {'image' : InlineImage(doc,'images/dunnoTest.jpg'), 'caption': 'I have no clue what this is'}]

todayStr = dt.datetime.now().strftime("%d-%b-%Y")

# create context to pass data to template
context = {
    "reportDtStr": todayStr,
    "processedImages": processedImages
}

# render context into the document object
doc.render(context)

# save the document object as a word file
reportWordPath = 'reports/report_{0}.docx'.format(todayStr)
doc.save(reportWordPath)

# convert the word file as pdf file
convert(reportWordPath, reportWordPath.replace(".docx", ".pdf"))
