https://medium.com/@jesvinkjustin/from-zero-to-rag-the-art-of-document-chunking-and-embedding-for-rag-d9764695cc46

From Zero to RAG: The Art of Document Chunking and Embedding for RAG
Jesvin K Justin
Jesvin K Justin
10 min read
·
Apr 19, 2025

Retrieval-Augmented Generation (RAG) is transforming how we interact with documents. Instead of making LLMs memorize everything, we give them the ability to retrieve only the relevant chunks of data, making them smarter, faster, and cheaper to run.

If you’re planning to build a RAG-based chatbot that works with Word, Excel, PDFs, and more, this post walks you through everything from the basics.
What is Document Chunking?

Chunking is the process of splitting large documents into smaller, manageable pieces — called “chunks” for easier embedding, searching, and response generation.

For instance, if you have a lengthy 100-page document, you might break it down into different sections, each potentially answering different user questions.

This way, each chunk of data is focused on a specific topic. When a piece of information is retrieved from the source dataset, it is more likely to be directly applicable to the user’s query, since we avoid including irrelevant information from entire documents.

This also improves efficiency, since the system can quickly obtain the most relevant pieces of information instead of processing entire documents.

For example:

    A 10-page PDF becomes 30 chunks of 300 characters each.
    Each chunk is embedded and stored in a database for retrieval.

How to Chunk a Document?
1. Fixed-Size Chunking

Fixed-size chunking is the most basic and straightforward method of dividing text. It segments the document into chunks based on a specified number of characters, without considering the semantic meaning or structure of the content. This method is simple but often results in chunks that may cut across sentences or paragraphs.

Frameworks like LangChain and LlamaIndex provide built-in utilities for this method, such as the CharacterTextSplitter and SentenceSplitter (which, by default, splits on sentence boundaries but can be configured for character-based chunking).

Key configuration options to understand:

    How the text is split: At the character level
    Measurement unit: Number of characters per chunk
    chunk_size: Total characters allowed in each chunk
    chunk_overlap: Number of overlapping characters between chunks (helps preserve context across boundaries)
    separator: The character(s) used to split text, defaulting to "" (empty string) for character-level splitting

This method is useful for its simplicity and speed, especially when working with small or unstructured datasets. However, it may compromise contextual understanding in downstream tasks.

Example

Text:

    “Artificial Intelligence is transforming industries. It has applications in healthcare, finance, education, and more. Machine learning, a subset of AI, enables systems to learn from data and improve over time.”

Chunking Logic: Split every 50 characters with 10-character overlap

    Chunk 1: Artificial Intelligence is transforming industr
    Chunk 2: ng industries. It has applications in healthca
    Chunk 3: ions in healthcare, finance, education, and mo

This ignores sentence structure but is simple and fast.
2. Recursive Chunking

While fixed-size chunking is simple to implement, it often ignores the natural structure of the text. Recursive chunking provides a more refined approach by intelligently breaking text using a hierarchy of separators.

In this method, the text is split recursively using a prioritized list of separators — such as paragraphs, newlines, spaces, and eventually characters. If the initial splitting does not yield chunks within the desired size, the method continues to recursively split the text further using the next separator in the list. This ensures that chunks are as meaningful and structured as possible while still fitting within the target size.

The LangChain framework supports this technique through its RecursiveCharacterTextSplitter class. It uses a default list of separators like ["\n\n", "\n", " ", ""] to progressively segment the content in a hierarchical manner.

This method is particularly effective when working with documents that have varying formats and lengths, as it balances both structure and size constraints.

Original Text:

### Introduction
Artificial Intelligence is growing rapidly.

### Applications
AI is used in healthcare and education.

Chunking Logic:

The Recursive Chunking strategy uses a list of separators in order to split the text:

    Try splitting by \n\n (double newline)

2. If chunks are still too large, split by \n (single newline)

3. If still too large, split by space ' '

4. If still too large, split by characters ('')

This preserves the semantic structure as much as possible while still keeping chunks within size limits.
Resulting Chunks:

🔹 Chunk 1:

### Introduction
Artificial Intelligence is growing rapidly.

🔹 Chunk 2:

### Applications
AI is used in healthcare and education.

3. Document-Based Chunking

Document-based chunking leverages the inherent structure of a document to segment it meaningfully. Unlike fixed or recursive chunking, this method considers the logical flow of content such as headings, code blocks, tables, or media elements. It works best with well-structured documents but may be less effective for raw or unstructured text.

Markdown Documents

For documents written in Markdown, LangChain offers the `MarkdownTextSplitter` class. This tool uses Markdown-specific elements like headings and bullet points as natural breakpoints for chunking, making it easier to preserve semantic structure.

Code Files (Python, JavaScript, etc.)

For source code files, LangChain provides the `PythonCodeTextSplitter`, which intelligently splits programs based on functions, classes, and definitions. Alternatively, you can use the `RecursiveCharacterTextSplitter` with the `from_language` method to specify languages like Python, JavaScript, etc., enabling syntax-aware chunking for various programming languages.

Documents with Tables

Tables can be challenging to chunk using basic methods because they risk losing the tabular context (row-column relationships). To maintain structure, it’s often helpful to reformat tables in a way that models can understand — using formats like HTML `<table>` tags or semicolon-separated CSV strings. For better semantic search performance, it’s common to summarize the table content after extraction, generate embeddings from that summary, and use it for retrieval instead of direct cell-level embeddings.

Documents with Images (Multimodal)

When handling documents with images, such as PDFs or reports, chunking needs to support multimodal content. Text and image embeddings are inherently different — although models like CLIP attempt to unify them. A more robust approach is to use multimodal models (e.g., GPT-4 Vision) to generate textual summaries of images and store embeddings of those summaries. Tools like `unstructured.io` provide methods like `partition_pdf` to extract both images and text from complex PDFs.
Examples

A: Markdown

# Introduction
Artificial Intelligence (AI) is transforming the world.

## Applications
AI is used in various domains like healthcare, education, and finance.

## Challenges
Despite its growth, AI faces issues like bias, lack of transparency, and ethical concerns.

Chunking Strategy:
Split the document using Markdown headers (#, ##, etc.) to preserve logical structure.

Resulting Chunks:

🔹 Chunk 1:

# Introduction
Artificial Intelligence (AI) is transforming the world.

🔹 Chunk 2:

## Applications
AI is used in various domains like healthcare, education, and finance.

🔹 Chunk 3:

## Challenges
Despite its growth, AI faces issues like bias, lack of transparency, and ethical concerns.

B: Python Code

def add(a, b):
    return a + b

class Calculator:
    def subtract(self, a, b):
        return a - b

Chunked as:

    Function: def add(a, b): return a + b
    Class: class Calculator: ...

C: Table

Reformatted as:

    <table><tr><td>Name</td><td>Age</td><td>Role</td></tr><tr><td>John</td><td>30</td><td>Dev</td></tr></table>

D: Image
Become a Medium member

Image of a brain scan — summarized using a vision model as:

    “This image shows a sagittal view of a healthy human brain.”

Then embedded as text.

This level of chunking is particularly powerful for domain-specific documents like research papers, legal contracts, source code, and structured datasets — where preserving content structure is critical for downstream tasks like semantic search and RAG-based chat systems.
4. Semantic Chunking

While the previous chunking levels focus on content length or structural cues, semantic chunking takes a more intelligent and adaptive approach. Instead of splitting text based solely on size or format, this method uses embedding-based similarity to understand and preserve the semantic coherence between chunks.

The key idea is to keep together sentences or sections that share a strong contextual or semantic relationship. This results in meaningfully grouping chunks, even if they vary in size.

How It Works:

Semantic chunking evaluates the similarity between sentences (or blocks of text) using embeddings, and dynamically chooses split points based on semantic divergence. It ensures that each chunk contains text that belongs together in meaning, rather than being arbitrarily cut by size constraints.

Tool Support:

LlamaIndex offers the ‘SemanticSplitterNodeParser’ class, which implements this technique. It uses contextual embedding similarity to decide where to place chunk boundaries, making it ideal for advanced use cases like RAG, summarization, or document question answering.

Key Parameters:

‘buffer_size’: Sets the size of the initial window used to scan the document. Larger buffers can capture broader context.

‘breakpoint_percentile_threshold’: Defines how aggressively or conservatively the chunker identifies breakpoints. Lower values lead to more splits.

‘embed_model /embed_mode’: Specifies the embedding model used to calculate semantic similarity (e.g., OpenAI, HuggingFace, etc.).

Example
Text:

“AI is the simulation of human intelligence by machines. It has applications across domains. For instance, in healthcare, AI is used for diagnosis and treatment planning. In finance, it’s used for fraud detection.”

Chunking Result (based on embedding similarity):

    Chunk 1: “AI is the simulation of human intelligence by machines. It has applications across domains.”
    Chunk 2: “For instance, in healthcare, AI is used for diagnosis and treatment planning.”
    Chunk 3: “In finance, it’s used for fraud detection.”

    Here, chunks are grouped by semantic themes.

Semantic chunking is particularly powerful for nuanced documents — like legal texts, medical records, or academic papers where maintaining meaning across paragraphs is more important than having uniformly sized chunks. While more computationally intensive, it significantly improves retrieval quality in RAG pipelines by keeping semantically aligned content together.
5. Agentic Chunking

Agentic chunking is an emerging and advanced strategy that leverages LLMs as decision-makers to dynamically determine _what_ content should be included in each chunk and _how much_ of it, based on contextual relevance. Unlike traditional methods that rely on fixed rules or embeddings alone, this approach introduces reasoning into the chunking process.

How It Works:

The process begins by generating propositions — standalone, self-contained statements extracted from raw text. This concept is inspired by academic research on breaking down documents into atomic, meaningful units. LangChain supports this with its built-in `propositional-retrieval` template, which facilitates extracting such propositions.

Once the propositions are extracted, they are passed through an LLM-based agent. This agent evaluates each proposition in context and decides:

- Whether it should be appended to an existing chunk based on semantic and logical continuity.

- Or whether it should start a new chunk, if it represents a distinct topic or context.

This method introduces agency and flexibility into the chunking process, enabling highly customized and intelligent chunk creation that mirrors human-like understanding.

Example
Text:

    “AI improves productivity. It automates tasks. However, it also raises ethical concerns. Bias in AI systems is a major issue.”

Propositions extracted:

1. AI improves productivity.

2. AI automates tasks.

3. AI raises ethical concerns.

4. Bias in AI systems is a major issue.

LLM Agent Decision:

- Chunk 1: “AI improves productivity. AI automates tasks.”

- Chunk 2: “AI raises ethical concerns. Bias in AI systems is a major issue.”

The agent groups propositions based on deeper understanding, not just proximity or format.

Agentic chunking is especially useful in knowledge-intensive applications, such as legal document analysis, policy review, or multi-turn RAG chat systems, where maintaining thematic consistency and contextual alignment is critical.
Challenges in Chunking

    Loss of context if chunks are too small.

    - Contextual bleeding if chunks are too large.

    - Formatting loss (tables, images) if naive text splitting is used.

    - Multi-language handling, OCR issues for images, and page breaks.

Chunking Word, Excel, PDF, PPT

You can’t treat all document types the same. Here’s how to handle them:

Format How to Extract

PDF: PyMuPDF, pdfplumber, unstructured.io

Word: docx2txt, python-docx, unstructured.io

Excel: pandas.read_excel() + convert to text

PPT: python-pptx, unstructured.io

    Best tool overall: Unstructured.io
    It parses documents while preserving layout — tables, headers, paragraphs, even OCR for images.

What is Metadata in Chunking?

When documents are split into smaller parts (chunks), we don’t just store the text — we also attach metadata to each chunk. Metadata is the additional information that gives context about that chunk. Think of it as a label or tag that helps you understand where the chunk came from and what it represents.
Common Metadata Fields:

    Document Name: Name or ID of the source document.
    Page Number: If the document is paginated (like a PDF), this shows which page the chunk came from.
    Chunk Number: The order of the chunk within the document.
    Content Type: Specifies if the chunk is a paragraph, table, title, image caption, etc.
    Date, Source, Author: Extra context like publication date, data source, or who wrote the content.

Why is Metadata Useful?

    Filtering Search: Want only chunks from tables or authored by a specific person? Use metadata filters!
    Tracing the Source: When a chunk is retrieved by the chatbot, metadata can tell you where in the original document it came from — helping with transparency and verification.
    Boosting Relevance: Metadata can improve search ranking. For instance, if the user asks for recent data, chunks with newer date metadata can be ranked higher.

In RAG-based systems, metadata plays a vital role in retrieval accuracy, result explainability, and content filtering. It’s like giving your chunks a smart identity tag!
Embedding the Chunks

After chunking, each chunk is converted into a vector using models like:

    sentence-transformers (free, offline)
    OpenAI embeddings (powerful, paid)
    Cohere, Google Palm, HuggingFace models, etc.

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunk_texts)

These vectors are then stored in a vector database.
Searching the Chunks

During a chat, your user’s query is also embedded and compared to all stored vectors to retrieve the most relevant chunks.

This is usually done using:

# Pseudo-code
query_vector = model.encode(user_query)
top_matches = vector_db.search(query_vector, top_k=3)

These matched chunks are passed to the LLM as context.
Best Vector Databases for RAG
Press enter or click to view image in full size
