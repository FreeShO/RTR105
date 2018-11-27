Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo.py", line 9, in <module>
    from numoy import random
ImportError: No module named numoy
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
>>> print(random.__doc__)

========================
Random Number Generation
========================

==================== =========================================================
Utility functions
==============================================================================
random_sample        Uniformly distributed floats over ``[0, 1)``.
random               Alias for `random_sample`.
bytes                Uniformly distributed random bytes.
random_integers      Uniformly distributed integers in a given range.
permutation          Randomly permute a sequence / generate a random sequence.
shuffle              Randomly permute a sequence in place.
seed                 Seed the random number generator.
choice               Random sample from 1-D array.

==================== =========================================================

==================== =========================================================
Compatibility functions
==============================================================================
rand                 Uniformly distributed values.
randn                Normally distributed values.
ranf                 Uniformly distributed floating point numbers.
randint              Uniformly distributed integers in a given range.
==================== =========================================================

==================== =========================================================
Univariate distributions
==============================================================================
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
chisquare            :math:`\chi^2` distribution.
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
gamma                Gamma distribution.
geometric            Geometric distribution.
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
laplace              Laplace distribution.
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
poisson              Poisson distribution.
power                Power distribution.
rayleigh             Rayleigh distribution.
triangular           Triangular distribution.
uniform              Uniform distribution.
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
==================== =========================================================

==================== =========================================================
Multivariate distributions
==============================================================================
dirichlet            Multivariate generalization of Beta distribution.
multinomial          Multivariate generalization of the binomial distribution.
multivariate_normal  Multivariate generalization of the normal distribution.
==================== =========================================================

==================== =========================================================
Standard distributions
==============================================================================
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
==================== =========================================================

==================== =========================================================
Internal functions
==============================================================================
get_state            Get tuple representing internal state of generator.
set_state            Set state of generator.
==================== =========================================================


>>> print(random.uniform.__doc__)]
SyntaxError: invalid syntax
>>> print(random.uniform.__doc__)

        uniform(low=0.0, high=1.0, size=None)

        Draw samples from a uniform distribution.

        Samples are uniformly distributed over the half-open interval
        ``[low, high)`` (includes low, but excludes high).  In other words,
        any value within the given interval is equally likely to be drawn
        by `uniform`.

        Parameters
        ----------
        low : float, optional
            Lower boundary of the output interval.  All values generated will be
            greater than or equal to low.  The default value is 0.
        high : float
            Upper boundary of the output interval.  All values generated will be
            less than high.  The default value is 1.0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : ndarray
            Drawn samples, with shape `size`.

        See Also
        --------
        randint : Discrete uniform distribution, yielding integers.
        random_integers : Discrete uniform distribution over the closed
                          interval ``[low, high]``.
        random_sample : Floats uniformly distributed over ``[0, 1)``.
        random : Alias for `random_sample`.
        rand : Convenience function that accepts dimensions as input, e.g.,
               ``rand(2,2)`` would generate a 2-by-2 array of floats,
               uniformly distributed over ``[0, 1)``.

        Notes
        -----
        The probability density function of the uniform distribution is

        .. math:: p(x) = \frac{1}{b - a}

        anywhere within the interval ``[a, b)``, and zero elsewhere.

        Examples
        --------
        Draw samples from the distribution:

        >>> s = np.random.uniform(-1,0,1000)

        All values are within the given interval:

        >>> np.all(s >= -1)
        True
        >>> np.all(s < 0)
        True

        Display the histogram of the samples, along with the
        probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 15, normed=True)
        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        >>> plt.show()

        
>>> random.uniform(0,1,5)
array([ 0.88620207,  0.46293607,  0.9489964 ,  0.71014049,  0.14736079])
>>> random.uniform(0,0.1,10)
array([ 0.03949918,  0.06333374,  0.09067325,  0.09673624,  0.04540816,
        0.00344156,  0.06834777,  0.04586786,  0.09016356,  0.01071186])
>>> random.uniform(0,0.1,10)
array([ 0.06194487,  0.06798489,  0.00152746,  0.06543185,  0.03584118,
        0.00780233,  0.01748087,  0.02431395,  0.04745879,  0.06648759])
>>> random.uniform(0,0.1,10)
array([ 0.06228458,  0.03907477,  0.00963674,  0.0944231 ,  0.09144161,
        0.0977415 ,  0.06152493,  0.07012654,  0.04379837,  0.01776478])
>>> random.uniform(0,0.1,10)
array([ 0.04181193,  0.0403068 ,  0.03227236,  0.07831165,  0.09276859,
        0.09420501,  0.01963031,  0.03282874,  0.07621082,  0.00416033])
>>> for i in range (10):
	int(random.uniform(0.100))

	
0
0
0
0
0
0
0
0
0
0
>>> for i in range (10):
	int(random.uniform(0,100))

	
89
49
62
40
19
99
70
4
68
17
>>> type(random.uniform(0,0.1,10))
<type 'numpy.ndarray'>
>>> type(random.uniform(0,100))
<type 'float'>
>>> random.seed(1)
>>> 
>>> random.unform(0,1,5)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    random.unform(0,1,5)
AttributeError: 'module' object has no attribute 'unform'
>>> random.seed(1)
>>> random.uniform(0,1,5)
array([  4.17022005e-01,   7.20324493e-01,   1.14374817e-04,
         3.02332573e-01,   1.46755891e-01])
>>> random.uniform(0,1,5)
array([ 0.09233859,  0.18626021,  0.34556073,  0.39676747,  0.53881673])
>>> random.uniform(0,1,5)
array([ 0.41919451,  0.6852195 ,  0.20445225,  0.87811744,  0.02738759])
>>> random.uniform(0,1,5)
array([ 0.67046751,  0.4173048 ,  0.55868983,  0.14038694,  0.19810149])
>>> random.uniform(0,1,5)
array([ 0.80074457,  0.96826158,  0.31342418,  0.69232262,  0.87638915])
>>> random.uniform(0,1,5)
array([ 0.89460666,  0.08504421,  0.03905478,  0.16983042,  0.8781425 ])
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo.py", line 27, in <module>
    k[4] = k[4] +1
IndexError: list index out of range
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
>>> k
[19, 24, 21, 17, 19]
>>> sum(k)
100
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
[11, 17, 22, 28, 22]
100
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
[21, 19, 18, 25, 17]
100
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
[14, 25, 28, 24, 9]
100
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
[16, 24, 13, 24, 23]
100
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
[25, 22, 13, 17, 23]
100
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo.py", line 36, in <module>
    plt.grind()
AttributeError: 'module' object has no attribute 'grind'
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo.py", line 36, in <module>
    plt.grind()
AttributeError: 'module' object has no attribute 'grind'
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo.py", line 42, in <module>
    N1 = N1 +1
NameError: name 'N1' is not defined
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo.py", line 49, in <module>
    S_nezinaamais = 1. * S_zinaamas * N1/N
NameError: name 'S_zinaamas' is not defined
>>> 
================== RESTART: /home/user/RTR105/MonteCarlo.py ==================
12.6075
>>> 
