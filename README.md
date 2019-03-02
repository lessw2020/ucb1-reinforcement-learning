# ucb1-reinforcement-learning
My implementation of Jeremy Kun's implementation of UCB1.  This is optimal selection algorithm under uncertainty and focuses on 'regret minimization' to optimize selections over time.

Purpose - I am working on integrating somme aspects of Reinforcement Learning into conventional deep learning for optimal hyper-paramater selection (i.e. learning rate, batch size, etc).

A key algorithm for this is UCB1.  The name is derived from Upper Confidence Bounds, which is a way (and one of the best after reading a number of thesis, papers, etc) of balancing the tension of exploration vs exploitation in order to optimize your results given the uncertainty of various choices.

My implementation is a re-write variation of Jeremy Kun's excellent code to help me understand it better.  Please see his article here:
https://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/
