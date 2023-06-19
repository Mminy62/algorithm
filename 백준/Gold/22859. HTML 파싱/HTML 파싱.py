import re
html_doc = input()

html_doc = html_doc[len('<main>'): -len('</main>')]

html_doc = re.sub(r'<div +title="([\w ]*)">', r'title : \1\n', html_doc)
html_doc = re.sub(r'</div>', '', html_doc)

html_doc = re.sub(r'<p>', '', html_doc)
html_doc = re.sub(r'</p>', '\n', html_doc)

html_doc = re.sub(r'</?[\w ]*>', '', html_doc)
html_doc = re.sub(r' ?\n ?', '\n', html_doc) # space 이거나 space + \n이거나
html_doc = re.sub(r' {2,}', ' ', html_doc) #' '{2,} #바로 앞 문자열 n개 이상 반복 AB{2,}	ABB, ABBB, ..

print(html_doc)