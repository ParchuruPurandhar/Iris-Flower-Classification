{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7957f07f-7a0e-4be4-8b0a-7515bfad6ea7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model Saved Successfully!\n"
     ]
    }
   ],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import pickle\n",
    "\n",
    "iris = load_iris()\n",
    "\n",
    "X = iris.data\n",
    "y = iris.target\n",
    "\n",
    "model = RandomForestClassifier(\n",
    "    n_estimators=100,\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "model.fit(X, y)\n",
    "\n",
    "pickle.dump(\n",
    "    model,\n",
    "    open(\"iris_model.pkl\", \"wb\")\n",
    ")\n",
    "\n",
    "print(\"Model Saved Successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d7b6dfc-5215-4f7c-8113-4369d2b0053b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
