{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_ _ _ _ _ _ _ _ _ _ \n",
      "_ _ _ _ _ _ _ _ _ _ \n",
      "_ e _ _ _ _ _ _ _ e \n",
      "_ e _ _ _ _ a _ _ e \n",
      "_ e _ i _ _ a _ _ e \n",
      "r e _ i _ _ a _ _ e \n",
      "r e _ i _ _ a _ _ e \n",
      "r e s i s _ a _ _ e \n",
      "r e s i s _ a _ _ e \n",
      "r e s i s _ a _ _ e \n",
      "r e s i s t a _ _ e \n",
      "r e s i s t a _ _ e \n",
      "r e s i s t a _ _ e \n",
      "r e s i s t a _ _ e \n",
      "r e s i s t a n _ e \n",
      "r e s i s t a n _ e \n",
      "r e s i s t a n c e \n",
      "r e s i s t a n c e \n",
      "r e s i s t a n c e \n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "words = ['father', 'enterprise', 'science', 'programming', \n",
    "         'resistance', 'fiction', 'condition', 'reverse', \n",
    "         'computer', 'python']\n",
    "word = random.choice(words)\n",
    "\n",
    "guesses = ''\n",
    "\n",
    "turns = 10\n",
    "\n",
    "while turns > 0:\n",
    "    for i in word:\n",
    "        if i in guesses:\n",
    "            print(i, end=' ')\n",
    "        else:\n",
    "            print('_', end=' ')\n",
    "    print()\n",
    "\n",
    "    guess = input(\"Guess a char: \")\n",
    "    guesses = guesses + guess"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
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
   "version": "3.11.3"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
