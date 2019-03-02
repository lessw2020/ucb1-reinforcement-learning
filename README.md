# ucb1-reinforcement-learning
My implementation of Jeremy Kun's implementation of UCB1.  This is optimal selection algorithm under uncertainty and focuses on 'regret minimization' to optimize selections over time.

Purpose - I am working on integrating some aspects of Reinforcement Learning into conventional deep learning for optimal hyper-paramater selection (i.e. learning rate, batch size, etc).

A key algorithm for this is UCB1.  The name is derived from Upper Confidence Bounds, which is a way (and one of the best after reading a number of thesis, papers, etc) of balancing the tension of exploration vs exploitation in order to optimize your results given the uncertainty of various choices.

UCB is basically = Estimated payoff for this action + (total plays / total times this action has been played), or + confidence factor.

Payoff so far + confidence of that payoff
Q(a) + sqrt((2 * log total actions taken)/number of times this action taken))

Each time we pick action a, it's uncertainty decreases as we have more data to get the likely actual reward from that action.

Conversely, the more we play other actions relative to a, the more the relative uncertainty estimate of the reward for a increases.

The log is used so that increases of uncertainty get smaller over time, relative to the total number of plays so far. 
We will thus implicitly reduce the use of actions that have lower payoffs as our confidence about their respective payoffs increases,as well as not pick those that have already beeen selected a lot (higher confidence bound) in order to eventually discover all the payoffs for this time section, and utilize the optimal action the most.

My implementation is a re-write variation of Jeremy Kun's excellent code to help me understand it better.  Please see his article and sample code here:
https://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/
