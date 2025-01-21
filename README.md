# OpenAISemanticAnalysis

This is a combination of multiple Python libraries to enhance the capabilities of Sentence-BERT. The goal was for the AI to be able to access and decipher two different PDF files with tables, datasets, etc. and fine the semantic similarities and differences, giving back a detailed explanation as to what is different between the two.

Sentence-BERT on its own is not capable of actually giving us an analysis output we can work with- it's very limited. First of all, its only return type is tensors, and secondly, it can't read charts or even any sort of text files. You can only give it simple str sentences so it can compare the literal difference between the two. So, I spent a long time finding different Python libraries and trying to piece together a method to utilize Sentence-BERT's limited functionality and be able to get a desirable output using it with other tools.
So, I ended up importing a few other libraries:
•	sentence-transformers
•	openai
•	PyPDF2
•	Pandas
These all have their own respective capabilities, here is how they all work together to get an ideal output:
 
1.	PyPDF2 extracts the raw text from the PDF files for "Repository 1" and "Repository 2". It will convert the PDFs into string format, which makes it usable for further analysis.
2.	Pandas will then take that extracted text, which is now just raw text, and shape it back into a structured format as it was in the PDF originally. It'll restore all the structured elements such as tables, statistics or numerical data.
3.	Sentence-BERT now will take the extracted and organized text from Repositories 1 and 2 respectively, and encode it into numerical representations. It converts plain text into embeddings and is able to capture the semantic meaning as well as the differences between the two files and the information within.
4.	OpenAI finally is able to take that extracted and processed data as input. It'll use a GPT-based model to generate a human-readable analysis of the comparison. It will take the instructions you've given it as well as the content to be able to provide a detailed explanation of the differences. It also handles both numerical and qualitative differences.
