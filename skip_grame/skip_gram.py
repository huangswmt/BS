import numpy as np
import tensorflow.compat.v1 as tf
import os
import time
import random
tf.disable_v2_behavior()
#import utils

class Train_data_load(object):
    def __init__(self):
        pass
    
    def init_key(self,keypath):
        workey=np.load(keypath,allow_pickle=True)
        workey = list(set(workey))
        int_to_vocab = {j:i for i,j in zip(workey,range(len(workey)))}
        word2int = {int_to_vocab[i]:i for i in int_to_vocab}
        
        self.int_to_vocab = int_to_vocab
        self.word2int = word2int
        self.workey = workey
    
    def init_data(self,datapath):
        alllist = np.load(datapath,allow_pickle=True)
        self . alllist = alllist
        
    def trans_2_int(self):
        alllist = self . alllist
        train_wordslist = []
        for wo in alllist:
            train_words =[self.word2int[i] for i in wo if (i in self.word2int) ]
            if len(train_words)>2:
                train_wordslist.append(train_words)
        self . train_wordslist = train_wordslist

        
    def get_target(self, words, idx, window_size=5):
       # ''' Get a list of words in a window around an index. '''

        R = np.random.randint(1, window_size+1)
        #print(R)
        start = idx - R if (idx - R) > 0 else 0
        stop = idx + R
        target_words = set(words[start:idx] + words[idx+1:stop+1])

        return list(target_words)    
    
    
    def get_batches(self, batch_size, window_size=5):
        ''' Create a generator of word batches as a tuple (inputs, targets) '''

        #n_batches = len(words)//batch_size

        # only full batches
        #words = words[:n_batches*batch_size]
        wordsl = self.train_wordslist
        all_batch = []
        for words in ( (wordsl)):
            if len(words)>batch_size:
                n_batches = len(words)//batch_size
                words = words[:n_batches*batch_size]
                for idx in range(0, len(words), batch_size):
                    x, y = [], []
                    batch = words[idx:idx+batch_size]
                    for ii in range(len(batch)):
                        batch_x = batch[ii]
                        batch_y = self.get_target(batch, ii, window_size)
                        y.extend(batch_y)
                        x.extend([batch_x]*len(batch_y))
                    yield x, y
            else:
                x, y = [], []
                batch = words
                for ii in range(len(batch)):
                    batch_x = batch[ii]
                    batch_y = self.get_target(batch, ii, window_size)
                    y.extend(batch_y)
                    x.extend([batch_x]*len(batch_y))

                yield x, y
                
                
    def train_s(self,n_embedding = 20,n_sampled = 5,epochs = 40,batch_size = 1000,window_size = 10,ch_save = "checkpoints_close/text8.ckpt",savename='w2v_mat'):
    
        loglist = []
        
        
        valid_size = 5# Random set of words to evaluate similarity on.
        valid_window = 200
        
        word2int = self.word2int
        train_graph = tf.Graph()
        with train_graph.as_default():
            inputs = tf.placeholder(tf.int32, [None], name='inputs')
            labels = tf.placeholder(tf.int32, [None, 1], name='labels')

        n_vocab = len(word2int)
        # Number of embedding features 
        with train_graph.as_default():
            embedding = tf.Variable(tf.random_uniform((n_vocab, n_embedding), -1, 1))
            embed = tf.nn.embedding_lookup(embedding, inputs)
        n_vocab

        # Number of negative labels to sample

        with train_graph.as_default():
            softmax_w = tf.Variable(tf.truncated_normal((n_vocab, n_embedding), stddev=0.1))
            softmax_b = tf.Variable(tf.zeros(n_vocab))

            # Calculate the loss using negative sampling
            loss = tf.nn.sampled_softmax_loss(softmax_w, softmax_b, 
                                              labels, embed,
                                              n_sampled, n_vocab)

            cost = tf.reduce_mean(loss)
            optimizer = tf.train.AdamOptimizer().minimize(cost)

        with train_graph.as_default():
            ## From Thushan Ganegedara's implementation

            # pick 8 samples from (0,100) and (1000,1100) each ranges. lower id implies more frequent 
            valid_examples = np.array(random.sample(range(valid_window), valid_size//2))
            valid_examples = np.append(valid_examples, 
                                       random.sample(range(1000,1000+valid_window), valid_size//2))

            valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

            # We use the cosine distance:
            norm = tf.sqrt(tf.reduce_sum(tf.square(embedding), 1, keepdims =True))
            normalized_embedding = embedding / norm
            valid_embedding = tf.nn.embedding_lookup(normalized_embedding, valid_dataset)
            similarity = tf.matmul(valid_embedding, tf.transpose(normalized_embedding))

        # If the checkpoints directory doesn't exist:
        #!mkdir checkpoints_close

        with train_graph.as_default():
            saver = tf.train.Saver()

        with tf.Session(graph=train_graph) as sess:
            iteration = 1
            loss = 0
            sess.run(tf.global_variables_initializer())

            for e in range(1, epochs+1):
                batches = self.get_batches(batch_size)
                start = time.time()
                for x, y in batches:

                    feed = {inputs: x,
                            labels: np.array(y)[:, None]}
                    train_loss, _ = sess.run([cost, optimizer], feed_dict=feed)

                    loss += train_loss

                    if iteration % 200 == 0: 
                        end = time.time()
                        print("Epoch {}/{}".format(e, epochs),
                              "Iteration: {}".format(iteration),
                              "Avg. Training loss: {:.4f}".format(loss/100),
                              "{:.4f} sec/batch".format((end-start)/100))
                        loss = 0
                        loglist.append(loss/100)
                        start = time.time()

                    if iteration % 400 == 0:
                        try:
                            # note that this is expensive (~20% slowdown if computed every 500 steps)
                            sim = similarity.eval()
                            for i in range(valid_size):
                                valid_word = int_to_vocab[valid_examples[i]]
                                top_k = 4 # number of nearest neighbors
                                nearest = (-sim[i, :]).argsort()[1:top_k+1]
                                log = 'Nearest to %s:' % valid_word
                                for k in range(top_k):

                                    close_word = int_to_vocab[nearest[k]]
                                    log = '%s %s,' % (log, close_word)
                                print(log)

                        except:
                            print('error')

                    iteration += 1
            save_path = saver.save(sess, ch_save)
            embed_mat = sess.run(normalized_embedding)
            self.embed_mat = embed_mat
            np.save(savename,embed_mat)
    def auto_train(self,datapath,keypath,\
                   n_embedding = 20,\
                   n_sampled = 5,\
                    epochs = 40,\
                   batch_size = 1000,\
                   window_size = 10,\
                    ch_save = "checkpoints_close/text8.ckpt",\
                  savename='w2v_mat'):
        
        self.init_data(datapath)
        self.init_key(keypath)
        self.trans_2_int()
        self.train_s(n_embedding,n_sampled,\
                      epochs ,batch_size,window_size ,\
                      ch_save ,\
                    savename)