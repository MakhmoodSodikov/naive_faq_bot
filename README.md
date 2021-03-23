# naive_faq_bot

Data - WikiQA dataset


Model - RNN seq2vec by deeppavlov


curl --header "Content-Type: application/json" \
--request POST \
--data '{"query":"where can I buy this item?"}' \
 http://$SERVER_IP:5001/model/test_api_external
