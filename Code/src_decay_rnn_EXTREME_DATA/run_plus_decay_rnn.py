from agreement_acceptor_decay_rnn import FullGramSentence
import filenames

pvn = FullGramSentence(filenames.deps, prop_train=0.8, output_filename='output_log.txt', len_after_verb=10)

pvn.pipeline(train=True,model="decay_fullGram_EXTREME.pkl", load_data=True,epochs=10, model_prefix='decay_fullGram_EXTREME', data_name='fullGram', test_size=7000)