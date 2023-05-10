{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "gender = input(\"What is your gender (M/F): \")\n",
    "gender = gender.upper()\n",
    "\n",
    "if gender == \"M\":\n",
    "    print(\"Male\")\n",
    "    age = input(\"What is your age?: \")\n",
    "    age = int(age)\n",
    "    if age <= 26:\n",
    "        print(\"Less/eaqual to 26\")\n",
    "        percentage = 23\n",
    "        market_price = input(\"What is the market price of your car? \")\n",
    "        market_price = int(market_price)\n",
    "        ensurance_offer = market_price*percentage/100\n",
    "        print(f\"Ensurance offer: {ensurance_offer}\")\n",
    "    else:\n",
    "        print(\"More than 26\")\n",
    "        percentage = 9\n",
    "        market_price = input(\"What is the market price of your car? \")\n",
    "        market_price = int(market_price)\n",
    "        ensurance_offer = market_price*percentage/100\n",
    "        print(f\"Ensurance offer: {ensurance_offer}\")\n",
    "elif gender == \"F\":\n",
    "    print(\"Female\")\n",
    "    car_type = input(\"What is your car type (S/N): \")\n",
    "    car_type = car_type.upper()\n",
    "    if car_type == \"S\":\n",
    "        print(\"Sport car\")\n",
    "        percentage = 21\n",
    "        market_price = input(\"What is the market price of your car? \")\n",
    "        market_price = int(market_price)\n",
    "        ensurance_offer = market_price*percentage/100\n",
    "        print(f\"Ensurance offer: {ensurance_offer}\")\n",
    "    elif car_type == \"N\":\n",
    "        print(\"None sport car\")\n",
    "        percentage = 10\n",
    "        market_price = input(\"What is the market price of your car? \")\n",
    "        market_price = int(market_price)\n",
    "        ensurance_offer = market_price*percentage/100\n",
    "        print(f\"Ensurance offer: {ensurance_offer}\")\n",
    "    else:\n",
    "        print(\"Wrong answer!\")\n",
    "else:\n",
    "    print(\"Wrong answer!\")"
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
