from sentence_transformers import SentenceTransformer
import json

def filter():
    model = SentenceTransformer("Snowflake/snowflake-arctic-embed-m-long", trust_remote_code=True)

    ###HERE ARE FILTER CRITERIA
    queries = ['mars colonisaion', 'progress on the Neutron rocket by rocket lab']
   
    documents = []
    f = open('data_sink.json')
    data = json.load(f)
    for i in data['articles']:
        documents.append(i['title'])  
        

    query_embeddings = model.encode(queries, prompt_name="query")
    document_embeddings = model.encode(documents)

    scores = query_embeddings @ document_embeddings.T

    #[print(score, document) for score, document in zip(scores, documents)]
    top_articles = {}
    for query, query_scores in zip(queries, scores):
        doc_score_pairs = list(zip(documents, query_scores))
        doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
        # Output passages & scores
        # print("Query:", query)
        # print(" title with top1 score ", doc_score_pairs[0][1], doc_score_pairs[0][0])
        #in json data , find "url" field which mathces top title , return top title and url 
        for i in data['articles']:
            if i['title'] == doc_score_pairs[0][0]:
                #  print("url:", i['url'])
                doc_score_pairs[0][0], i['url']
                top_articles[doc_score_pairs[0][0]] = i['url']
                 
                 
    return top_articles


if __name__ == "__main__":
    print(filter())
