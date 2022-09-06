{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import matplotlib.pyplot as plt \n",
    "from scipy import stats\n",
    "\n",
    "def q_x_given_y(y, mean_p, cov_p):\n",
    "\n",
    "    muy = mean_p[0] + cov_p[1, 0] / cov_p[0, 0] * (y - mean_p[1])\n",
    "    sigma = cov_p[0, 0] - cov_p[1, 0] / cov_p[1, 1] * cov_p[1, 0]\n",
    "    proposed_state = np.random.normal(muy, sigma)\n",
    "    return proposed_state\n",
    "\n",
    "\n",
    "def q_y_given_x(x, mean_p, cov_p):\n",
    " \n",
    "    muy = mean_p[1] + cov_p[0, 1] / cov_p[1, 1] * (x - mean_p[0])\n",
    "    sigma = cov_p[1, 1] - cov_p[0, 1] / cov_p[0, 0] * cov_p[0, 1]\n",
    "    proposed_state = np.random.normal(muy, sigma)\n",
    "    return proposed_state\n",
    "\n",
    "\n",
    "def gibbs_sampling_2d_normal_distribution(mean_p, cov_p, n, init):\n",
    "   \n",
    "    samples = np.zeros(shape=(n, 2))\n",
    "    samples[0] = init\n",
    "\n",
    "    for i in range(n-1):\n",
    "        y = samples[i, 1]\n",
    "        x = q_x_given_y(y, mean_p, cov_p)\n",
    "        samples[i+1, :] = np.array([x, y])\n",
    "        y = q_y_given_x(x, mean_p, cov_p)\n",
    "        samples[i+1, :] = [x, y]\n",
    "    return samples\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    n = 10000\n",
    "    init = np.array([2, 2.5])\n",
    "    mean_p = np.array([3, 4])\n",
    "    cov_p = np.array([[1.0, 0.7],\n",
    "                      [0.7,1.2]])\n",
    "    samples = gibbs_sampling_2d_normal_distribution(mean_p, cov_p, n, init)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
