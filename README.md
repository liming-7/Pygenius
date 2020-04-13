# Pygenius
The python general negotion platform for researchers.

### Development Process
**Core**
- [ ] Core Agent(Negotiator) info. 
- [ ] Core domain, issue, value class.
- [ ] Core protocol, SAOP and Mediator interface.
- [ ] Core action (Accept, Leave, Offer.). 
- [ ] xml2json parser: This is to transfer xml domain to json.
- [ ] logging, visualize, checkpoint.

**Library**
- [ ] Analysis Library, given the domain and Analysis the features of the domain.
- [ ] Strategy Library, 1. Reuse genius ANAC library(use Py4j?)  2. Offer space for following strategies in ANAC.
- [ ] Protocol Library, protocol mainly defines the way of the game/negotiation.   

**Intergrate to GeniusWeb**
- [ ] Flask Server using our framework, which can be a strategy server of GeniusWeb. (Conneted to GeniusWeb.)
- [ ] Enable Tensorboard. 


### Features
1. Easy install, can use 'pip install' same as other python package, like Pytorch. 
2. Json based data format. Including message, domain, profile. The model(strategy) trained on PyGenius can be easily transfered to GeniusWeb. At the same time, we can write a adapter party on geniusweb to use the strategy write in Pygenius framework. 
3. Users can easily use deep reinforcement learning to train a dynamic strategy. (Online training)
4. Protocol: Bilateral and Mediator based. The we offer flexible mediator API, users can write their mediator(actor). This is mainly for the actor-critc method of reinforcement learning, can help us develop cooperate strategy and open research area of many new fields of multi-agent (Deep reinforcement learning), such as Credit assignment, adhoc team play, self-play...
5. Basic Strategy Library: Offer basic strategy. User can use API.
6. Standard Negotiation test domain Library: Offer the general test domain for negotiation agents.
7. Offer peer simulator function, consider the network cost and time cost in real world.(Not quite sure)
8. The domain, utilitysapce, utilityfunction can not only load from related profile, but also also be defined in the program.
