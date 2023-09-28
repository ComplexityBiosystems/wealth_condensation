# wealth_condensation
Python module to study simple agent based models of wealth condensation. 

(c) Stefano Zapperi 2023

The model was used to obtain the results in:

C. A. M. La Porta and S. Zapperi, 
Unraveling the dynamics of wealth inequality and the impact on social mobility and health disparities
J. Phys. Complexity 2023

#### Dependencies
numpy 
scipy
pandas 
matplotlib
seaborn
networkx https://pypi.org/project/networkx/
sdeint https://pypi.org/project/sdeint/


#### Model
The model proposed by JPB&MM (Bouchaud, J. P., & Mézard, M. (2000). Wealth condensation in a simple model of economy. Physica A: Statistical Mechanics and its Applications, 282(3-4), 536-545. https://www.sciencedirect.com/science/article/pii/S0378437100002053 ) in the variant proposed by JPB that includes taxes and the governement (Bouchaud, J. P. (2015). On growth-optimal tax rates and the issue of wealth inequalities. Journal of Statistical Mechanics: Theory and Experiment, 2015(11), P11011. https://iopscience.iop.org/article/10.1088/1742-5468/2015/11/P11011/pdf)

In the continuum version of the model, we consider a random interaction network schematized by an adjaciency matrix $$A^0_{ij}=A^0_{ji}$$.
The random network is a regular random graph of degree $c$ but other choices are possible.

he equations of the model are the following for individuals:

$$ dW_i/dt = \eta_i(t) W_i + J_0\sum_j A^0_{ij}(W_j -W_i) - \phi W_i + f/N V$$

where parameters are: 
N number of agents
$$W_i$$ (w[i]) wealth of individual i
$$\phi$$ (phi) tax rate
f tax redistribution rate
$$J_{ij}=J_0$$ is a constant
V state wealth
$$\eta_i(t)$$ (eta[i]) Gaussian random noise with mean m and variance s.

The equation for the state is

$$dV/dt =  \sigma  \xi(t)  V + \phi W + (\mu-f)V$$

where:
- W is the total wealth
- xi is the noise (with mean 0 and variance 1)
- (sigma) is the real variance and  (mu) is the mean

To solve the model is convenient to express it in terms of an 
(N+1)-dimensional system of equations for the vector 
$$X = (W_0, ...., W_{N-1}, V)$$
which obeys

$$dX_i = \sum_j A_{ij} X_j dt + B_i X_i d\psi_i$$

where:
$$A_{ij} = A^0_{ij}J_0 + \delta_{ij} (m-J_0\sum_k A^0_{ki} -\phi)  \mbox{ for } i,j=0,N-1$$   
$$A_{iN}=f/N, i \lt N$$ 
$$A_{Ni}=\phi, i\lt N$$
$$A_{NN}=(\mu-f)$$
$$B_i = s,  i \lt N$$
$$B_i=\sigma, i=N$$
$$d\psi_i$$ are independent Wiener processes (with variance 1 and zero mean)
