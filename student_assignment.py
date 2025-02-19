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
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    full_text = "\n".join(doc.page_content for doc in documents)

    #splitter = RecursiveCharacterTextSplitter(["第","章", "條","\n", "\n\n", " "], 200, 10)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=40, 
        chunk_overlap=0,  
        separators=[
            r"第 \s*.+\s*章",
            r"第\s*\d+-?\d*\s*條"
        ],
        is_separator_regex=True  # 啟用正則表達式
    )
    
    chunks = text_splitter.split_text(full_text)

    if chunks:
        number_of_chunks = len(chunks)
        print(f"總共有 {number_of_chunks} 個 chunks\n")

        for i in range(number_of_chunks):
            print(f"Chunk {i+1}:\n {chunks[i]}")
    else:
        print("未能分割PDF文件。")

    return number_of_chunks

if __name__ == "__main__":
    hw02_2(q2_pdf)


