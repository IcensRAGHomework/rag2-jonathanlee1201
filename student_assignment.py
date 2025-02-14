from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=0)
    chunks = splitter.split_documents(documents)

    if chunks:
        last_chunk = chunks[-1]
        print("最後一個chunk的內容:")
        print(last_chunk.page_content)
    else:
        print("未能分割PDF文件。")

    return last_chunk
   

def hw02_2(q2_pdf):
    pass

if __name__ == "__main__":
    hw02_1(q1_pdf)


