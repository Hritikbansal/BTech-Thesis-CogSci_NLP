from agreement_acceptor import FullGramSentence
import filenames

pvn = FullGramSentence(filenames.deps, prop_train=0.8, output_filename='output_log.txt',batch_size=128, len_after_verb=10, embedding_size=650, hidden_dim = 650)
pvn.pipeline(train=True, load_data=True, epochs=40, model_prefix='lstm_fullGram',test_size=7000, data_name='fullGram')
