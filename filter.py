from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-m-long", trust_remote_code=True)




queries = ['mars colonisaion', 'rocket lab company', 'progress on the Neutron rocket by rocket lab']
# documents = [".)", "SpaceX reached another milestone when booster B1062 became the first in its fleet to fly for the 21st time on Friday night, exceeding the previously set limit of 20 flights per booster. Blue Origin also launched its first crewed mission for over 18 months on Sunday, taking six more humans briefly above the Karman line. The crew included former Air Force Captain Ed Dwight, who is about a week older than William Shatner, and became the oldest person to fly in space"]
documents = []
f = open('data_sink.json')
data = json.load(f)
for i in data['articles']:
    documents.append(i['title'] + " " +i['content'] )  

query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)

scores = query_embeddings @ document_embeddings.T

[print(score, document) for score, document in zip(scores, documents)]


# for query, query_scores in zip(queries, scores):
#     doc_score_pairs = list(zip(documents, query_scores))
#     doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
#     # Output passages & scores
#     print("Query:", query)
#     for document, score in doc_score_pairs:
#         print(score, document)