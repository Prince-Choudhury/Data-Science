{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('Algerian_forest_fires_cleaned_dataset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>Temperature</th>\n",
       "      <th>RH</th>\n",
       "      <th>Ws</th>\n",
       "      <th>Rain</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>BUI</th>\n",
       "      <th>FWI</th>\n",
       "      <th>Classes</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>2012</td>\n",
       "      <td>29</td>\n",
       "      <td>57</td>\n",
       "      <td>18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>65.7</td>\n",
       "      <td>3.4</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>3.4</td>\n",
       "      <td>0.5</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>2012</td>\n",
       "      <td>29</td>\n",
       "      <td>61</td>\n",
       "      <td>13</td>\n",
       "      <td>1.3</td>\n",
       "      <td>64.4</td>\n",
       "      <td>4.1</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.9</td>\n",
       "      <td>0.4</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "      <td>2012</td>\n",
       "      <td>26</td>\n",
       "      <td>82</td>\n",
       "      <td>22</td>\n",
       "      <td>13.1</td>\n",
       "      <td>47.1</td>\n",
       "      <td>2.5</td>\n",
       "      <td>7.1</td>\n",
       "      <td>0.3</td>\n",
       "      <td>2.7</td>\n",
       "      <td>0.1</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>2012</td>\n",
       "      <td>25</td>\n",
       "      <td>89</td>\n",
       "      <td>13</td>\n",
       "      <td>2.5</td>\n",
       "      <td>28.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>6.9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.7</td>\n",
       "      <td>0.0</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>2012</td>\n",
       "      <td>27</td>\n",
       "      <td>77</td>\n",
       "      <td>16</td>\n",
       "      <td>0.0</td>\n",
       "      <td>64.8</td>\n",
       "      <td>3.0</td>\n",
       "      <td>14.2</td>\n",
       "      <td>1.2</td>\n",
       "      <td>3.9</td>\n",
       "      <td>0.5</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   day  month  year  Temperature  RH  Ws  Rain  FFMC  DMC    DC  ISI  BUI  \\\n",
       "0    1      6  2012           29  57  18   0.0  65.7  3.4   7.6  1.3  3.4   \n",
       "1    2      6  2012           29  61  13   1.3  64.4  4.1   7.6  1.0  3.9   \n",
       "2    3      6  2012           26  82  22  13.1  47.1  2.5   7.1  0.3  2.7   \n",
       "3    4      6  2012           25  89  13   2.5  28.6  1.3   6.9  0.0  1.7   \n",
       "4    5      6  2012           27  77  16   0.0  64.8  3.0  14.2  1.2  3.9   \n",
       "\n",
       "   FWI      Classes  Region  \n",
       "0  0.5  not fire          0  \n",
       "1  0.4  not fire          0  \n",
       "2  0.1  not fire          0  \n",
       "3  0.0  not fire          0  \n",
       "4  0.5  not fire          0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain', 'FFMC',\n",
       "       'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes', 'Region'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "##drop month,day and yyear\n",
    "df.drop(['day','month','year'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Temperature</th>\n",
       "      <th>RH</th>\n",
       "      <th>Ws</th>\n",
       "      <th>Rain</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>BUI</th>\n",
       "      <th>FWI</th>\n",
       "      <th>Classes</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29</td>\n",
       "      <td>57</td>\n",
       "      <td>18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>65.7</td>\n",
       "      <td>3.4</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>3.4</td>\n",
       "      <td>0.5</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>29</td>\n",
       "      <td>61</td>\n",
       "      <td>13</td>\n",
       "      <td>1.3</td>\n",
       "      <td>64.4</td>\n",
       "      <td>4.1</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.9</td>\n",
       "      <td>0.4</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>26</td>\n",
       "      <td>82</td>\n",
       "      <td>22</td>\n",
       "      <td>13.1</td>\n",
       "      <td>47.1</td>\n",
       "      <td>2.5</td>\n",
       "      <td>7.1</td>\n",
       "      <td>0.3</td>\n",
       "      <td>2.7</td>\n",
       "      <td>0.1</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>25</td>\n",
       "      <td>89</td>\n",
       "      <td>13</td>\n",
       "      <td>2.5</td>\n",
       "      <td>28.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>6.9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.7</td>\n",
       "      <td>0.0</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>27</td>\n",
       "      <td>77</td>\n",
       "      <td>16</td>\n",
       "      <td>0.0</td>\n",
       "      <td>64.8</td>\n",
       "      <td>3.0</td>\n",
       "      <td>14.2</td>\n",
       "      <td>1.2</td>\n",
       "      <td>3.9</td>\n",
       "      <td>0.5</td>\n",
       "      <td>not fire</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Temperature  RH  Ws  Rain  FFMC  DMC    DC  ISI  BUI  FWI      Classes  \\\n",
       "0           29  57  18   0.0  65.7  3.4   7.6  1.3  3.4  0.5  not fire      \n",
       "1           29  61  13   1.3  64.4  4.1   7.6  1.0  3.9  0.4  not fire      \n",
       "2           26  82  22  13.1  47.1  2.5   7.1  0.3  2.7  0.1  not fire      \n",
       "3           25  89  13   2.5  28.6  1.3   6.9  0.0  1.7  0.0  not fire      \n",
       "4           27  77  16   0.0  64.8  3.0  14.2  1.2  3.9  0.5  not fire      \n",
       "\n",
       "   Region  \n",
       "0       0  \n",
       "1       0  \n",
       "2       0  \n",
       "3       0  \n",
       "4       0  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fire             131\n",
       "not fire         101\n",
       "fire               4\n",
       "fire               2\n",
       "not fire           2\n",
       "not fire           1\n",
       "not fire           1\n",
       "not fire           1\n",
       "Name: Classes, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Classes'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Encoding\n",
    "df['Classes']=np.where(df['Classes'].str.contains(\"not fire\"),0,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Temperature</th>\n",
       "      <th>RH</th>\n",
       "      <th>Ws</th>\n",
       "      <th>Rain</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>BUI</th>\n",
       "      <th>FWI</th>\n",
       "      <th>Classes</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>238</th>\n",
       "      <td>30</td>\n",
       "      <td>65</td>\n",
       "      <td>14</td>\n",
       "      <td>0.0</td>\n",
       "      <td>85.4</td>\n",
       "      <td>16.0</td>\n",
       "      <td>44.5</td>\n",
       "      <td>4.5</td>\n",
       "      <td>16.9</td>\n",
       "      <td>6.5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>239</th>\n",
       "      <td>28</td>\n",
       "      <td>87</td>\n",
       "      <td>15</td>\n",
       "      <td>4.4</td>\n",
       "      <td>41.1</td>\n",
       "      <td>6.5</td>\n",
       "      <td>8.0</td>\n",
       "      <td>0.1</td>\n",
       "      <td>6.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>27</td>\n",
       "      <td>87</td>\n",
       "      <td>29</td>\n",
       "      <td>0.5</td>\n",
       "      <td>45.9</td>\n",
       "      <td>3.5</td>\n",
       "      <td>7.9</td>\n",
       "      <td>0.4</td>\n",
       "      <td>3.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>24</td>\n",
       "      <td>54</td>\n",
       "      <td>18</td>\n",
       "      <td>0.1</td>\n",
       "      <td>79.7</td>\n",
       "      <td>4.3</td>\n",
       "      <td>15.2</td>\n",
       "      <td>1.7</td>\n",
       "      <td>5.1</td>\n",
       "      <td>0.7</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>242</th>\n",
       "      <td>24</td>\n",
       "      <td>64</td>\n",
       "      <td>15</td>\n",
       "      <td>0.2</td>\n",
       "      <td>67.3</td>\n",
       "      <td>3.8</td>\n",
       "      <td>16.5</td>\n",
       "      <td>1.2</td>\n",
       "      <td>4.8</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Temperature  RH  Ws  Rain  FFMC   DMC    DC  ISI   BUI  FWI  Classes  \\\n",
       "238           30  65  14   0.0  85.4  16.0  44.5  4.5  16.9  6.5        1   \n",
       "239           28  87  15   4.4  41.1   6.5   8.0  0.1   6.2  0.0        0   \n",
       "240           27  87  29   0.5  45.9   3.5   7.9  0.4   3.4  0.2        0   \n",
       "241           24  54  18   0.1  79.7   4.3  15.2  1.7   5.1  0.7        0   \n",
       "242           24  64  15   0.2  67.3   3.8  16.5  1.2   4.8  0.5        0   \n",
       "\n",
       "     Region  \n",
       "238       1  \n",
       "239       1  \n",
       "240       1  \n",
       "241       1  \n",
       "242       1  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    137\n",
       "0    106\n",
       "Name: Classes, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Classes'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Independent And dependent features\n",
    "X=df.drop('FWI',axis=1)\n",
    "y=df['FWI']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Temperature</th>\n",
       "      <th>RH</th>\n",
       "      <th>Ws</th>\n",
       "      <th>Rain</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>BUI</th>\n",
       "      <th>Classes</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29</td>\n",
       "      <td>57</td>\n",
       "      <td>18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>65.7</td>\n",
       "      <td>3.4</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>3.4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>29</td>\n",
       "      <td>61</td>\n",
       "      <td>13</td>\n",
       "      <td>1.3</td>\n",
       "      <td>64.4</td>\n",
       "      <td>4.1</td>\n",
       "      <td>7.6</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>26</td>\n",
       "      <td>82</td>\n",
       "      <td>22</td>\n",
       "      <td>13.1</td>\n",
       "      <td>47.1</td>\n",
       "      <td>2.5</td>\n",
       "      <td>7.1</td>\n",
       "      <td>0.3</td>\n",
       "      <td>2.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>25</td>\n",
       "      <td>89</td>\n",
       "      <td>13</td>\n",
       "      <td>2.5</td>\n",
       "      <td>28.6</td>\n",
       "      <td>1.3</td>\n",
       "      <td>6.9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>27</td>\n",
       "      <td>77</td>\n",
       "      <td>16</td>\n",
       "      <td>0.0</td>\n",
       "      <td>64.8</td>\n",
       "      <td>3.0</td>\n",
       "      <td>14.2</td>\n",
       "      <td>1.2</td>\n",
       "      <td>3.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Temperature  RH  Ws  Rain  FFMC  DMC    DC  ISI  BUI  Classes  Region\n",
       "0           29  57  18   0.0  65.7  3.4   7.6  1.3  3.4        0       0\n",
       "1           29  61  13   1.3  64.4  4.1   7.6  1.0  3.9        0       0\n",
       "2           26  82  22  13.1  47.1  2.5   7.1  0.3  2.7        0       0\n",
       "3           25  89  13   2.5  28.6  1.3   6.9  0.0  1.7        0       0\n",
       "4           27  77  16   0.0  64.8  3.0  14.2  1.2  3.9        0       0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      0.5\n",
       "1      0.4\n",
       "2      0.1\n",
       "3      0.0\n",
       "4      0.5\n",
       "      ... \n",
       "238    6.5\n",
       "239    0.0\n",
       "240    0.2\n",
       "241    0.7\n",
       "242    0.5\n",
       "Name: FWI, Length: 243, dtype: float64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Train Test Split\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((182, 11), (61, 11))"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape,X_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Temperature</th>\n",
       "      <th>RH</th>\n",
       "      <th>Ws</th>\n",
       "      <th>Rain</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>BUI</th>\n",
       "      <th>Classes</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Temperature</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.656095</td>\n",
       "      <td>-0.305977</td>\n",
       "      <td>-0.317512</td>\n",
       "      <td>0.694768</td>\n",
       "      <td>0.498173</td>\n",
       "      <td>0.390684</td>\n",
       "      <td>0.629848</td>\n",
       "      <td>0.473609</td>\n",
       "      <td>0.542141</td>\n",
       "      <td>0.254549</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RH</th>\n",
       "      <td>-0.656095</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.225736</td>\n",
       "      <td>0.241656</td>\n",
       "      <td>-0.653023</td>\n",
       "      <td>-0.414601</td>\n",
       "      <td>-0.236078</td>\n",
       "      <td>-0.717804</td>\n",
       "      <td>-0.362317</td>\n",
       "      <td>-0.456876</td>\n",
       "      <td>-0.394665</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ws</th>\n",
       "      <td>-0.305977</td>\n",
       "      <td>0.225736</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.251932</td>\n",
       "      <td>-0.190076</td>\n",
       "      <td>0.000379</td>\n",
       "      <td>0.096576</td>\n",
       "      <td>-0.023558</td>\n",
       "      <td>0.035633</td>\n",
       "      <td>-0.082570</td>\n",
       "      <td>-0.199969</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rain</th>\n",
       "      <td>-0.317512</td>\n",
       "      <td>0.241656</td>\n",
       "      <td>0.251932</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.545491</td>\n",
       "      <td>-0.289754</td>\n",
       "      <td>-0.302341</td>\n",
       "      <td>-0.345707</td>\n",
       "      <td>-0.300964</td>\n",
       "      <td>-0.369357</td>\n",
       "      <td>-0.059022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FFMC</th>\n",
       "      <td>0.694768</td>\n",
       "      <td>-0.653023</td>\n",
       "      <td>-0.190076</td>\n",
       "      <td>-0.545491</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.620807</td>\n",
       "      <td>0.524101</td>\n",
       "      <td>0.750799</td>\n",
       "      <td>0.607210</td>\n",
       "      <td>0.781259</td>\n",
       "      <td>0.249514</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DMC</th>\n",
       "      <td>0.498173</td>\n",
       "      <td>-0.414601</td>\n",
       "      <td>0.000379</td>\n",
       "      <td>-0.289754</td>\n",
       "      <td>0.620807</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.868647</td>\n",
       "      <td>0.685656</td>\n",
       "      <td>0.983175</td>\n",
       "      <td>0.617273</td>\n",
       "      <td>0.212582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DC</th>\n",
       "      <td>0.390684</td>\n",
       "      <td>-0.236078</td>\n",
       "      <td>0.096576</td>\n",
       "      <td>-0.302341</td>\n",
       "      <td>0.524101</td>\n",
       "      <td>0.868647</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.513701</td>\n",
       "      <td>0.942414</td>\n",
       "      <td>0.543581</td>\n",
       "      <td>-0.060838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ISI</th>\n",
       "      <td>0.629848</td>\n",
       "      <td>-0.717804</td>\n",
       "      <td>-0.023558</td>\n",
       "      <td>-0.345707</td>\n",
       "      <td>0.750799</td>\n",
       "      <td>0.685656</td>\n",
       "      <td>0.513701</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.643818</td>\n",
       "      <td>0.742977</td>\n",
       "      <td>0.296441</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BUI</th>\n",
       "      <td>0.473609</td>\n",
       "      <td>-0.362317</td>\n",
       "      <td>0.035633</td>\n",
       "      <td>-0.300964</td>\n",
       "      <td>0.607210</td>\n",
       "      <td>0.983175</td>\n",
       "      <td>0.942414</td>\n",
       "      <td>0.643818</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.612239</td>\n",
       "      <td>0.114897</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Classes</th>\n",
       "      <td>0.542141</td>\n",
       "      <td>-0.456876</td>\n",
       "      <td>-0.082570</td>\n",
       "      <td>-0.369357</td>\n",
       "      <td>0.781259</td>\n",
       "      <td>0.617273</td>\n",
       "      <td>0.543581</td>\n",
       "      <td>0.742977</td>\n",
       "      <td>0.612239</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.188837</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Region</th>\n",
       "      <td>0.254549</td>\n",
       "      <td>-0.394665</td>\n",
       "      <td>-0.199969</td>\n",
       "      <td>-0.059022</td>\n",
       "      <td>0.249514</td>\n",
       "      <td>0.212582</td>\n",
       "      <td>-0.060838</td>\n",
       "      <td>0.296441</td>\n",
       "      <td>0.114897</td>\n",
       "      <td>0.188837</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Temperature        RH        Ws      Rain      FFMC       DMC  \\\n",
       "Temperature     1.000000 -0.656095 -0.305977 -0.317512  0.694768  0.498173   \n",
       "RH             -0.656095  1.000000  0.225736  0.241656 -0.653023 -0.414601   \n",
       "Ws             -0.305977  0.225736  1.000000  0.251932 -0.190076  0.000379   \n",
       "Rain           -0.317512  0.241656  0.251932  1.000000 -0.545491 -0.289754   \n",
       "FFMC            0.694768 -0.653023 -0.190076 -0.545491  1.000000  0.620807   \n",
       "DMC             0.498173 -0.414601  0.000379 -0.289754  0.620807  1.000000   \n",
       "DC              0.390684 -0.236078  0.096576 -0.302341  0.524101  0.868647   \n",
       "ISI             0.629848 -0.717804 -0.023558 -0.345707  0.750799  0.685656   \n",
       "BUI             0.473609 -0.362317  0.035633 -0.300964  0.607210  0.983175   \n",
       "Classes         0.542141 -0.456876 -0.082570 -0.369357  0.781259  0.617273   \n",
       "Region          0.254549 -0.394665 -0.199969 -0.059022  0.249514  0.212582   \n",
       "\n",
       "                   DC       ISI       BUI   Classes    Region  \n",
       "Temperature  0.390684  0.629848  0.473609  0.542141  0.254549  \n",
       "RH          -0.236078 -0.717804 -0.362317 -0.456876 -0.394665  \n",
       "Ws           0.096576 -0.023558  0.035633 -0.082570 -0.199969  \n",
       "Rain        -0.302341 -0.345707 -0.300964 -0.369357 -0.059022  \n",
       "FFMC         0.524101  0.750799  0.607210  0.781259  0.249514  \n",
       "DMC          0.868647  0.685656  0.983175  0.617273  0.212582  \n",
       "DC           1.000000  0.513701  0.942414  0.543581 -0.060838  \n",
       "ISI          0.513701  1.000000  0.643818  0.742977  0.296441  \n",
       "BUI          0.942414  0.643818  1.000000  0.612239  0.114897  \n",
       "Classes      0.543581  0.742977  0.612239  1.000000  0.188837  \n",
       "Region      -0.060838  0.296441  0.114897  0.188837  1.000000  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Feature Selection based on correlaltion\n",
    "X_train.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot: >"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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BolEgqtXr6J169aFFScRERERERFpmXw1KC9fvoyDBw+iQ4cOmDx5MipXroyqVati06ZNhRQeERERERFRPuTzNgz6PDr5yRwUFIQaNWoAACpWrAh9fX2MG5fzw2eJiIiIiIjo65WvBqVCoYBYnD5VsVAohJGRkcaDIiIiIiIiIu2XryGvSqUSo0aNUj1DUiKRYOLEiVkalWfPau8U+ERERERE9BXjLK9FKl8NypEjR6q9Hz58uEaDISIiIiIioi9HvhqUBw8eLKw4iIiIiIiI6AuTrwYlERERERGRVuMsr0UqX5PyEBEREREREf2HDUoiIiIiIiIqEA55JSIiIiKirwdneS1S7KEkIiIiIiKiAmGDkoiIiIiIiAqEQ16JiIiIiOjrwVleixR7KImIiIiIiKhA2KAkIiIiIiKiAuGQVyIiIiIi+npwltcixR5KIiIiIiIiKhA2KImIiIiIiKhAOOSViIiIiIi+HhzyWqTYQ0lEREREREQFwgYlERERERERFQiHvBIRERER0ddDqSzuCP6vsIeSiIiIiIiICoQNSiIiIiIiIioQDnklIiIiIqKvB2d5LVLsoSQiIiIiIqICYYOSiIiIiIiICoRDXomIiIiI6OvBIa9FSmsalL0s6xZ3CFrDt9Wk4g5Bq5S7t7O4Q9AqgR0mFHcIWmOyVZPiDkGrNJAKijsErWKbIivuELTGt1ZtizsErWIqkxd3CFrDV2xW3CFoFX8h6wZRfnHIKxERERERERWI1vRQEhERERERfTYlh7wWJfZQEhERERERUYGwQUlEREREREQFwiGvRERERET09eAsr0WKPZRERERERERUIGxQEhERERERUYFwyCsREREREX09lMrijuD/CnsoiYiIiIiIqEDYoCQiIiIiIqIC4ZBXIiIiIiL6enCW1yLFHkoiIiIiIiIqEDYoiYiIiIiIqEA45JWIiIiIiL4eHPJapNhDSURERERERAXCBiUREREREREVCIe8EhERERHR10PJIa9FiT2UREREREREVCBsUBIREREREVGBcMgrERERERF9NZQKZXGH8H+FPZRERERERERUIGxQEhERERERUYFwyCsREREREX09FJzltSixh5KIiIiIiIgKhA1KIiIiIiIiKhAOeSUiIiIioq+HkkNeixJ7KImIiIiIiKhAPrtBKZfL8eLFC0RHR2siHiIiIiIi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8/PDxIkTAaQNn/3+++9V+YcOHQpLS0uMHj0a7969w7179zBnzhyMGTOmUCflyfM9lAqFAk5OTrhz5w5u376Nf//9F4mJibC3t0fbtm2xfft2tG3bttACJSIiIiIi+n8xaNAgREZGYsWKFQgODkatWrVw5coVlCtXDgAQHBys9kzKEiVK4ObNm5g2bRoaNWoES0tLDBw4EKtWrSrUOPPcoDQzM0NiYiLs7OzQpk0b/Pbbb2jbti0qVapUmPERERERERH9X5o8eTImT56c7WeHDh3KkvbNN99kGSZb2PLcoNywYQPatm2LqlWrFmY8REREREREBafU3llev0Z5blBOmKC9z3MhIiIiIiKiolfgSXmIiIiIiIjo/1ueeyiJiIiIiIi0Xj5nU6XPwx5KIiIiIiIiKhA2KImIiIiIiKhAOOSViIiIiIi+GkoFZ3ktSuyhJCIiIiIiogJhg5KIiIiIiIgKhENeiYiIiIjo68FZXosUeyiJiIiIiIioQNigJCIiIiIiogLhkFciIiIiIvp6KDnLa1FiDyUREREREREVCBuUREREREREVCAc8kpERERERF8PzvJapNhDSURERERERAXCBiUREREREREVCIe8EhERERHR10PBWV6LEnsoiYiIiIiIqEDYoCQiIiIiIqIC4ZBXIiIiIiL6enCW1yLFHkoiIiIiIiIqEK3poZSDVxL+oyPktsgosMOE4g5Bq9j/vbu4Q9Aaf1YfWNwhaJUQo3LFHYJWSVXyWPqfZMQVdwhaxUggLu4QtEaUQlrcIWiVXqlmxR0C0RdHaxqUREREREREn03JWV6LEoe8EhERERERUYGwQUlEREREREQFwiGvRERERET09eAsr0WKPZRERERERERUIGxQEhERERERUYFwyCsREREREX01lArO8lqU2ENJREREREREBcIGJRERERERERUIh7wSEREREdHXg7O8Fin2UBIREREREVGBsEFJREREREREBcIhr0RERERE9PXgkNcixR5KIiIiIiIiKhA2KImIiIiIiKhAOOSViIiIiIi+HkpFcUfwf4U9lERERERERFQgbFASERERERFRgXDIKxERERERfT04y2uRYg8lERERERERFQgblERERERERFQgHPJKRERERERfDSWHvBYp9lASERERERFRgRS4h/Kff/7BP//8g7CwMCgU6s96OXDgwGcH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tWvo06cPO5RERERERFR2lJwxWZqKNEJpZGQEkSi/Lzp06FAsXrwYAQEB8PT0LLbgiIiIiIiIyHAVqkOZmpqKkSNHwtHREW5ubli/fj2USiWWLl2KKlWq4NatW9ixY0dJxUpEREREREQGpFBTXhcvXowrV65g7NixOHv2LObMmYOzZ88iNzcXp0+fRrt27UoqTiIiIiIiov+k4pTXUlWoDuWpU6ewc+dOdO7cGdOmTUPVqlXh6emJdevWlVB4REREREREZKgKNeU1OjoatWrVAgBUrlwZpqammDRpUokERkRERERERIatUCOUSqUSYnH+w4CFQiEsLCyKPSgiIiIiIqIi4ZTXUlWoDqVKpcK4ceNgYmICAMjNzcXUqVN1OpWHDx8uvgiJiIiIiIjIIBWqQzl27Fit96NGjSrWYIiIiIiIiOjtUagO5c6dO0sqDiIiIiIiojenLOsA3i+FWpSHiIiIiIiI6F/sUBIREREREVGRFGrKKxERERERkSFTcZXXUsURSiIiIiIiIgO0efNmeHh4wNTUFI0bN8bVq1dfq9z169chEonQoEGDkg0Q7FASEREREREZnH379mH27NlYsmQJvL290aZNG/To0QPh4eGvLJeWloYxY8agU6dOpRInO5RERERERPTuUKoM9iWVSpGenq71kkqlequxdu1aTJw4EZMmTULNmjWxbt06uLu746effnpl9adMmYIRI0bAy8urJL5dHexQEhERERERlYKVK1dCIpFovVauXKmTTyaT4d69e+jatatWeteuXXHjxo0Ct79z504EBQVh2bJlxR57QbgoDxERERERUSlYtGgR5s6dq5VmYmKiky8xMREKhQLOzs5a6c7OzoiNjdW77YCAACxcuBBXr16FSFR63Tx2KImIiIiI6N2hLOsACmZiYqK3A1kQgUCg9V6lUumkAYBCocCIESOwfPlyeHp6vnGchcEOJRERERERkQFxcHCAUCjUGY2Mj4/XGbUEgIyMDNy9exfe3t6YMWMGAECpVEKlUkEkEuH8+fPo2LFjicTKeyiJiIiIiIgMiLGxMRo3bowLFy5opV+4cAEtW7bUyW9tbY2HDx/Cx8dH85o6dSqqV68OHx8fNG/evMRi5QglERERERG9M1RKVVmHUCzmzp2L0aNHo0mTJvDy8sK2bdsQHh6OqVOnAlDfjxkVFYU9e/bAyMgIderU0Srv5OQEU1NTnfTixg4lERERERGRgRk2bBiSkpLw5ZdfIiYmBnXq1MHp06dRsWJFAEBMTMx/PpOyNAhUKpVBdOFHVBxQ1iEYjBXWWWUdgkExEhrELmowyv25taxDMBi1aw4t6xAMSiuLimUdgkGRG8bPm0HIgbysQzAoFgJxWYdgMJKV+p9/977qq7Qp6xAMyuTIX8s6hCJJGdK+rEMokO2BS2UdQrHjCCUREREREb07DHiV13cRF+UhIiIiIiKiImGHkoiIiIiIiIrEYKa8/vxtvbIOwWC4TH4756uXlGkOJbfM8dvoEO8b1Hj8dH9Zh2BQ8vatLesQDIoqNr6sQzAYRs1bl3UIBkUV5F/WIRgMQe0GZR2CQYmbd6isQ6Bi8K6s8vq24AglERERERERFQk7lERERERERFQkBjPllYiIiIiI6I1xlddSxRFKIiIiIiIiKhJ2KImIiIiIiKhIOOWViIiIiIjeGSpOeS1VHKEkIiIiIiKiImGHkoiIiIiIiIqEU16JiIiIiOjdwSmvpYojlERERERERFQk7FASERERERFRkXDKKxERERERvTO4ymvp4gglERERERERFQk7lERERERERFQknPJKRERERETvDk55LVUcoSQiIiIiIqIiYYeSiIiIiIiIioRTXomIiIiI6J3BVV5LF0coiYiIiIiIqEjYoSQiIiIiIqIiKVSH8uLFi6hVqxbS09N1PktLS0Pt2rVx9erVYguOiIiIiIioMFRKw329iwrVoVy3bh0mT54Ma2trnc8kEgmmTJmCtWvXFltwREREREREZLgK1aF88OABunfvXuDnXbt2xb179944KCIiIiIiIjJ8hVrlNS4uDmKxuOCNiURISEh446CIiIiIiIiK4l2dWmqoCjVCWa5cOTx8+LDAz319feHq6vrGQREREREREZHhK1SHsmfPnli6dClyc3N1PsvJycGyZcvQu3fvYguOiIiIiIiIDFehprx+9tlnOHz4MDw9PTFjxgxUr14dAoEAT58+xaZNm6BQKLBkyZKSipWIiIiIiOjVVIKyjuC9UqgOpbOzM27cuIGPPvoIixYtgkqlAgAIBAJ069YNmzdvhrOzc4kESkRERERERIalUB1KAKhYsSJOnz6NlJQUBAYGQqVSoVq1arC1tS2J+IiIiIiIiMhAFbpD+S9bW1s0bdq0OGMpdvvu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HxkRCbjxxa8IPJLfUa3YpRE6/JC/JkLnn2YCAO6uPYx7aw+XZLXpPSZQvequ8Zfs3LkTH3/8MY4dO4YOHbQXH7l48SL69++PjRs3ai1f+7pSC1jM5H209Pa7cQW7uAzOfbtG9kradhPFf2d6T2wZU+hJFu804aDCt73vMmH5gh9X8r6Rrpn/35neI8ZTDHul0NKUt2vNf2d6j/z6P2FZh2BQpkT+WtYhFMmecqPKOoQCjYl6O7/TVynUjYt79+7F4sWLdTqTANCxY0csXLgQv/32W7EFR0RERERERIarUB1KX19fdO9e8CMyevTogQcPDP95c0RERERERPTmCjVfLDk5Gc7OBS9T7ezsjJSUt3/FNiIiIiIiejvxZqnSVagRSoVCAZGo4D6oUCiEXC5/46CIiIiIiIjI8BV6lddx48bpPEPyX1KpYS+BT0RERERERMWnUB3KsWPH/meeoqzwSkREREREVBxe+xEWVCwK1aHcuXNnScVBREREREREb5lC3UNJRERERERE9C8+FZyIiIiIiN4ZSkFZR/B+4QglERERERERFQk7lERERERERFQk7FASERERERFRkfAeSiIiIiIiemcoyzqA9wxHKImIiIiIiKhI2KEkIiIiIiKiIuGUVyIiIiIiemdwymvp4gglERERERERFQk7lERERERERFQknPJKRERERETvDJWgrCN4v3CEkoiIiIiIiIqEHUoiIiIiIiIqEk55JSIiIiKidwZXeS1dHKEkIiIiIiKiImGHkoiIiIiIiIqEU16JiIiIiOidwSmvpYsjlERERERERFQk7FASERERERFRkXDKKxERERERvTNUZR3Ae4YjlERERERERFQkBjNCady+TlmHYDA2Hzlc1iEYlGYOHco6BIOSg/SyDsFgGDVvXdYhGBTV49tlHYJBke7bWdYhGAyTT1aXdQgGJe/whrIOwWAYNWpc1iEYlL6VTpV1CERvHYPpUBIREREREb0ppaCsI3i/cMorERERERERFQk7lERERERERFQknPJKRERERETvDGVZB/Ce4QglERERERERFQk7lERERERERFQknPJKRERERETvDE55LV0coSQiIiIiIqIiYYeSiIiIiIiIioRTXomIiIiI6J2hKusA3jMcoSQiIiIiIqIiYYeSiIiIiIiIioRTXomIiIiI6J2hFJR1BO8XjlASERERERFRkbBDSUREREREREXCKa9ERERERPTOUJZ1AO8ZjlASERERERFRkbBDSUREREREREXCKa9ERERERPTOUJV1AO8ZjlASERERERFRkbBDSUREREREREXCKa9ERERERPTOUHLSa6niCCUREREREREVCTuUREREREREVCSc8kpERERERO8MZVkH8J7hCCUREREREREVCTuUREREREREVCSc8kpERERERO8MrvFaujhCSUREREREREXyTo9Q7n8Qjt33QpGYJUMVewvMa1cDjcrZFphfJldi2+0gnPKLQVK2FM6WppjYrDL61y4HAPgrMA4/3wlBRGo25EolKthYYHTjiuhd0620qvTGln4+F5MmjoStrQR37nhj5sdL8OSJf4H5/7pwAO3atdRJP336L/TtPwYA8OmCGejfvwdqVK+KnJxc3Lx1F4sWfwN//6ASq0dR1PtkIKqO7ABjiQWSvINwZ/EupPlHvbKMe8+mqL9gMKwqOiEjLB4Pvj2AiLN3NZ/XntEHFXo2hXVVVyhyZUi4GwDvr/chPShG7/aafzcB1UZ3xN2lv8Dvf+eKtX5vaujs4eg8oissJJYI9PbH9s+3IDIgosD8zbt7YeD0wXCp6AqhWISYkGic2H4UV45c0trm0DnDtcqlxKdgctOxJVWNN7bv+mPsvvQAienZqOJii/n9WqJRZVe9eT/f+zdO3NU9fio72+LwgqEAgGN3nmHZvks6eW5/OxEmYsNvgvf9E4jdN58hMSMHVZwkmN+1ARpVdCwwv0yuwNYrT3D6YRgSM3PhbG2GSa1ron/DygCAPIUSO649xQnfUMSn56CSgxU+7lQPrarq/44NjahFNxi36QeBlS2U8RGQntwJZehTvXmFHrVh9uGXOulZa2dBlaBue4yc3GHc5QMYlasMI1snSE/uQN71UyVah9J21+chdv5+EE/8ApGQlIwfV36OTm11f1fedvt9wrD7n2AkZklRxd4S8zrUQqPydgXml8kV2HYrEKeeRCEpW6Y+52heBf3ruuvkPesXjUWnfNC+ijN+6N+4JKtRbPbdeKJuSzNyUMXZFvP7tii4Lf3jEk7cC9BJr+xsg8Pzhuikn/UJwsLfLqJ97YpYN65rscdeGswH9IPF8GEQ2ttDHhqKtB83Is/3od684np1YD11CkQV3SEwNYUiNg7Zx04ga//BUo6aSL9Cnc2s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\n",
      "text/plain": [
       "<Figure size 1200x1000 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Check for multicollinearity\n",
    "plt.figure(figsize=(12,10))\n",
    "corr=X_train.corr()\n",
    "sns.heatmap(corr,annot=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Temperature</th>\n",
       "      <th>RH</th>\n",
       "      <th>Ws</th>\n",
       "      <th>Rain</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>BUI</th>\n",
       "      <th>Classes</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Temperature</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.656095</td>\n",
       "      <td>-0.305977</td>\n",
       "      <td>-0.317512</td>\n",
       "      <td>0.694768</td>\n",
       "      <td>0.498173</td>\n",
       "      <td>0.390684</td>\n",
       "      <td>0.629848</td>\n",
       "      <td>0.473609</td>\n",
       "      <td>0.542141</td>\n",
       "      <td>0.254549</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RH</th>\n",
       "      <td>-0.656095</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.225736</td>\n",
       "      <td>0.241656</td>\n",
       "      <td>-0.653023</td>\n",
       "      <td>-0.414601</td>\n",
       "      <td>-0.236078</td>\n",
       "      <td>-0.717804</td>\n",
       "      <td>-0.362317</td>\n",
       "      <td>-0.456876</td>\n",
       "      <td>-0.394665</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ws</th>\n",
       "      <td>-0.305977</td>\n",
       "      <td>0.225736</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.251932</td>\n",
       "      <td>-0.190076</td>\n",
       "      <td>0.000379</td>\n",
       "      <td>0.096576</td>\n",
       "      <td>-0.023558</td>\n",
       "      <td>0.035633</td>\n",
       "      <td>-0.082570</td>\n",
       "      <td>-0.199969</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rain</th>\n",
       "      <td>-0.317512</td>\n",
       "      <td>0.241656</td>\n",
       "      <td>0.251932</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.545491</td>\n",
       "      <td>-0.289754</td>\n",
       "      <td>-0.302341</td>\n",
       "      <td>-0.345707</td>\n",
       "      <td>-0.300964</td>\n",
       "      <td>-0.369357</td>\n",
       "      <td>-0.059022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FFMC</th>\n",
       "      <td>0.694768</td>\n",
       "      <td>-0.653023</td>\n",
       "      <td>-0.190076</td>\n",
       "      <td>-0.545491</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.620807</td>\n",
       "      <td>0.524101</td>\n",
       "      <td>0.750799</td>\n",
       "      <td>0.607210</td>\n",
       "      <td>0.781259</td>\n",
       "      <td>0.249514</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DMC</th>\n",
       "      <td>0.498173</td>\n",
       "      <td>-0.414601</td>\n",
       "      <td>0.000379</td>\n",
       "      <td>-0.289754</td>\n",
       "      <td>0.620807</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.868647</td>\n",
       "      <td>0.685656</td>\n",
       "      <td>0.983175</td>\n",
       "      <td>0.617273</td>\n",
       "      <td>0.212582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DC</th>\n",
       "      <td>0.390684</td>\n",
       "      <td>-0.236078</td>\n",
       "      <td>0.096576</td>\n",
       "      <td>-0.302341</td>\n",
       "      <td>0.524101</td>\n",
       "      <td>0.868647</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.513701</td>\n",
       "      <td>0.942414</td>\n",
       "      <td>0.543581</td>\n",
       "      <td>-0.060838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ISI</th>\n",
       "      <td>0.629848</td>\n",
       "      <td>-0.717804</td>\n",
       "      <td>-0.023558</td>\n",
       "      <td>-0.345707</td>\n",
       "      <td>0.750799</td>\n",
       "      <td>0.685656</td>\n",
       "      <td>0.513701</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.643818</td>\n",
       "      <td>0.742977</td>\n",
       "      <td>0.296441</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BUI</th>\n",
       "      <td>0.473609</td>\n",
       "      <td>-0.362317</td>\n",
       "      <td>0.035633</td>\n",
       "      <td>-0.300964</td>\n",
       "      <td>0.607210</td>\n",
       "      <td>0.983175</td>\n",
       "      <td>0.942414</td>\n",
       "      <td>0.643818</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.612239</td>\n",
       "      <td>0.114897</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Classes</th>\n",
       "      <td>0.542141</td>\n",
       "      <td>-0.456876</td>\n",
       "      <td>-0.082570</td>\n",
       "      <td>-0.369357</td>\n",
       "      <td>0.781259</td>\n",
       "      <td>0.617273</td>\n",
       "      <td>0.543581</td>\n",
       "      <td>0.742977</td>\n",
       "      <td>0.612239</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.188837</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Region</th>\n",
       "      <td>0.254549</td>\n",
       "      <td>-0.394665</td>\n",
       "      <td>-0.199969</td>\n",
       "      <td>-0.059022</td>\n",
       "      <td>0.249514</td>\n",
       "      <td>0.212582</td>\n",
       "      <td>-0.060838</td>\n",
       "      <td>0.296441</td>\n",
       "      <td>0.114897</td>\n",
       "      <td>0.188837</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Temperature        RH        Ws      Rain      FFMC       DMC  \\\n",
       "Temperature     1.000000 -0.656095 -0.305977 -0.317512  0.694768  0.498173   \n",
       "RH             -0.656095  1.000000  0.225736  0.241656 -0.653023 -0.414601   \n",
       "Ws             -0.305977  0.225736  1.000000  0.251932 -0.190076  0.000379   \n",
       "Rain           -0.317512  0.241656  0.251932  1.000000 -0.545491 -0.289754   \n",
       "FFMC            0.694768 -0.653023 -0.190076 -0.545491  1.000000  0.620807   \n",
       "DMC             0.498173 -0.414601  0.000379 -0.289754  0.620807  1.000000   \n",
       "DC              0.390684 -0.236078  0.096576 -0.302341  0.524101  0.868647   \n",
       "ISI             0.629848 -0.717804 -0.023558 -0.345707  0.750799  0.685656   \n",
       "BUI             0.473609 -0.362317  0.035633 -0.300964  0.607210  0.983175   \n",
       "Classes         0.542141 -0.456876 -0.082570 -0.369357  0.781259  0.617273   \n",
       "Region          0.254549 -0.394665 -0.199969 -0.059022  0.249514  0.212582   \n",
       "\n",
       "                   DC       ISI       BUI   Classes    Region  \n",
       "Temperature  0.390684  0.629848  0.473609  0.542141  0.254549  \n",
       "RH          -0.236078 -0.717804 -0.362317 -0.456876 -0.394665  \n",
       "Ws           0.096576 -0.023558  0.035633 -0.082570 -0.199969  \n",
       "Rain        -0.302341 -0.345707 -0.300964 -0.369357 -0.059022  \n",
       "FFMC         0.524101  0.750799  0.607210  0.781259  0.249514  \n",
       "DMC          0.868647  0.685656  0.983175  0.617273  0.212582  \n",
       "DC           1.000000  0.513701  0.942414  0.543581 -0.060838  \n",
       "ISI          0.513701  1.000000  0.643818  0.742977  0.296441  \n",
       "BUI          0.942414  0.643818  1.000000  0.612239  0.114897  \n",
       "Classes      0.543581  0.742977  0.612239  1.000000  0.188837  \n",
       "Region      -0.060838  0.296441  0.114897  0.188837  1.000000  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def correlation(dataset, threshold):\n",
    "    col_corr = set()\n",
    "    corr_matrix = dataset.corr()\n",
    "    for i in range(len(corr_matrix.columns)):\n",
    "        for j in range(i):\n",
    "            if abs(corr_matrix.iloc[i, j]) > threshold: \n",
    "                colname = corr_matrix.columns[i]\n",
    "                col_corr.add(colname)\n",
    "    return col_corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "## threshold--Domain expertise\n",
    "corr_features=correlation(X_train,0.85)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'BUI', 'DC'}"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((182, 9), (61, 9))"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## drop features when correlation is more than 0.85 \n",
    "X_train.drop(corr_features,axis=1,inplace=True)\n",
    "X_test.drop(corr_features,axis=1,inplace=True)\n",
    "X_train.shape,X_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Scaling Or Standardization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "scaler=StandardScaler()\n",
    "X_train_scaled=scaler.fit_transform(X_train)\n",
    "X_test_scaled=scaler.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.84284248,  0.78307967,  1.29972026, ..., -0.62963326,\n",
       "        -1.10431526, -0.98907071],\n",
       "       [-0.30175842,  0.64950844, -0.59874754, ..., -0.93058524,\n",
       "        -1.10431526,  1.01105006],\n",
       "       [ 2.13311985, -2.08870172, -0.21905398, ...,  2.7271388 ,\n",
       "         0.90553851,  1.01105006],\n",
       "       ...,\n",
       "       [-1.9250106 ,  0.9166509 ,  0.54033314, ..., -1.06948615,\n",
       "        -1.10431526, -0.98907071],\n",
       "       [ 0.50986767, -0.21870454,  0.16063958, ...,  0.5973248 ,\n",
       "         0.90553851,  1.01105006],\n",
       "       [-0.57230045,  0.98343651,  2.05910739, ..., -0.86113478,\n",
       "        -1.10431526, -0.98907071]])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_scaled"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Box Plots To understand Effect Of Standard Scaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_1342/160744393.py:2: MatplotlibDeprecationWarning: Auto-removal of overlapping axes is deprecated since 3.6 and will be removed two minor releases later; explicitly call ax.remove() as needed.\n",
      "  plt.subplot(1, 2, 1)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'X_train After Scaling')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABMIAAAHBCAYAAACL2xepAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAACIS0lEQVR4nOzde1zUVf7H8fcwyAxewAuJFxTtYuWtErWUSu0imba2lZWCa2mtrXZB7Wa2hV2kTJTdLpbddAXNrqvtWuSv0lqyXdRMM9dyN1EqNFgTTQd15vz+cJllBBVwhi8z83o+HvN4wPme+X4/B4bhzOd7LjZjjBEAAAAAAAAQ4iKsDgAAAAAAAACoDyTCAAAAAAAAEBZIhAEAAAAAACAskAgDAAAAAABAWCARBgAAAAAAgLBAIgwAAAAAAABhgUQYAAAAAAAAwgKJMAAAAAAAAIQFEmEAAAAAAAAICyTCgHoyduxYORwObdy4scqxJ554QjabTe+++26Nz7do0SJlZ2f7MUJfnTp10k033eS3882fP182m83nccopp2jgwIH6y1/+UufzHjx4ULfddpvatm0ru92uc889128xn4xDhw7phRdeUJ8+fdSyZUs1btxYiYmJGj58uN55552AXXfgwIEaOHCgT5nNZlNGRkbArgkAAI4v3PuBlf3xj3+UzWZT9+7dj1nnwQcfVMeOHRUZGanmzZtr//79ysjI0MqVKwMS07GUlpZq6tSp6tq1q5o0aaLY2FidddZZGj16tDZs2BCw6x7dd1u5cqVsNlu9tx8IVTZjjLE6CCAclJWVqUePHmrVqpX+/ve/q1GjRpKkjRs3qnfv3ho1apReffXVGp9v2LBh+uqrr7Rt27aAxPvFF18oJiZGp512ml/ON3/+fN1888169dVXddZZZ8kYo+LiYj3zzDP66KOPtGzZMl111VW1Pu8f/vAHpaen6+mnn1ZSUpKaNm2qHj16+CXmk3HjjTfq7bffVnp6ugYOHCiHw6F///vfev/993XKKafo+eefD8h1K5JglTtKn3/+uRISEpSQkBCQawIAgOML935gZeeee66+/PJLSUf6KOeff77P8aVLl+rqq6/WtGnTNGTIEDkcDnXq1EmnnHKKHn744Xq7ubdv3z6dd9552rdvn+655x6dc845OnDggL755hu9/fbb+u1vf6vf/OY3Abm2zWbzaWtZWZm+/vprde3aVTExMQG5JhBOIq0OAAgXMTExevnllzV48GA99thjmj59ug4dOqTRo0crPj4+oHf13G63Dh8+LIfDUePnnHfeeQGJpXv37urdu7f3+yuuuEItWrTQ4sWL65QI++qrrxQdHa3bb7/dbzEeOHBA0dHRdX7+d999pyVLluihhx7S9OnTveWXXnqpbr31Vnk8Hn+EWWMXXHBBvV4PAAD4oh94xJo1a/Tll19q6NCh+utf/6qXX365SiLsq6++kiTdeeedat26tSSppKQkIPEcOnRINptNkZFVPxa/8cYb2rp1qz766CMNGjTI59jkyZPrtT8XExNDfw7wI6ZGAvXosssu02233aYZM2Zo7dq1ysjI0JdffqmXX35ZsbGxNT7PwIED9de//lWFhYU+Uw0ladu2bbLZbJo5c6Yee+wxde7cWQ6HQx9//LFcLpemTJmic889V7GxsWrZsqX69eunpUuXVrnG0UPiK4ZkL168WNOmTVO7du0UExOjyy67TFu2bKnzz8TpdCoqKsp7Z7TCwYMH9dhjj+mss86Sw+HQKaecoptvvlk//fSTt47NZtNLL72kAwcOeH8G8+fPlyS5XC5NnTpVnTt3VlRUlNq3b6+JEyfq559/rtLOYcOG6e2339Z5550np9PpTV4VFxdr/PjxSkhIUFRUlDp37qzp06fr8OHDx21TaWmpJKlt27bVHo+I8H3r/fnnnzVlyhSdeuqpcjgcat26ta688kr985//9NaZPn26zj//fLVs2VIxMTHq1auXXn75ZdVkUO/Rw+srpql+/PHH+t3vfqe4uDi1atVK11xzjX744Qef55aXl2vKlClq06aNGjdurIsvvlhr164N6JQJAABCEf1A6eWXX5Z0ZDpo//799dprr2n//v0+133wwQclSfHx8bLZbLrpppt0yimnSDrSH6pob+X4vv32W40aNUqtW7eWw+HQ2WefrWeffdbn2hVtWLhwoaZMmaL27dvL4XBo69at1cZa2/7cP//5T40cOVLx8fFyOBzq2LGjfvOb36i8vFyS9NNPP2nChAnq2rWrmjZtqtatW+uSSy7Rp59+esKfW3VTI2+66SY1bdpUW7du1ZVXXqmmTZuqQ4cOmjJliveaFYqKinTdddepWbNmat68uVJTU1VQUODTdwbCCSPCgHr21FNPKS8vT9ddd5127Nih2267TZdffnmtzvHcc8/pt7/9rf71r38dc72pP/7xj+rSpYtmzZqlmJgYnXHGGSovL9d//vMf3X333Wrfvr0OHjyo//u//9M111yjV199tUbDux944AElJyfrpZdeUllZme677z5dddVV2rx5s+x2+wmfX3FX0hijnTt36qmnntIvv/yiUaNGeet4PB4NHz5cn376qe699171799fhYWFevjhhzVw4ECtWbNG0dHRWr16tR599FF9/PHH+uijjyRJp512mowxuvrqq/Xhhx9q6tSpuuiii7RhwwY9/PDDWr16tVavXu1zV3TdunXavHmzHnzwQXXu3FlNmjRRcXGx+vbtq4iICD300EM67bTTtHr1aj322GPatm3bcacvnH322WrevLmmT5+uiIgIDR48WJ06daq27t69e3XhhRdq27Ztuu+++3T++edr3759+uSTT/Tjjz/qrLPOknSkYzt+/Hh17NhR0pGpBHfccYe+//57PfTQQyf8uVfnlltu0dChQ7Vo0SLt2LFD99xzj9LS0rw/S0m6+eabtWTJEt1777265JJL9PXXX+vXv/61ysrK6nRNAADCWTj3Aw8cOKDFixerT58+6t69u8aOHatbbrlFb7zxhsaMGSNJeuedd/Tss8/q5Zdf1vvvv6/Y2Fi1bdtWI0eO1BVXXKFx48bplltukSRvcuzrr79W//791bFjR2VlZalNmzbKy8vTnXfeqZKSEj388MM+cUydOlX9+vXT888/r4iICO+os6P169dPkvSb3/xGDzzwgC666CK1atWq2rpffvmlLrzwQsXFxemRRx7RGWecoR9//FHLli3TwYMH5XA49J///EeS9PDDD6tNmzbat2+f3nnnHQ0cOFAffvhhlTVea+LQoUP61a9+pXHjxmnKlCn65JNP9Oijjyo2NtbbP/zll180aNAg/ec//9GTTz6p008/Xe+//75uuOGGWl8PCBkGQL1btGiRkWTatGlj9u7dW6dzDB061CQmJlYp/+6774wkc9ppp5mDBw8e9xyHDx82hw4dMuPGjTPnnXeez7HExEQzZswY7/cff/yxkWSuvPJKn3qvv/66kWRWr1593Gu9+uqrRlKVh8PhMM8995xP3cWLFxtJ5q233vIpLygoMJJ86o8ZM8Y0adLEp977779vJJmZM2f6lC9ZssRIMvPmzfNpp91uN1u2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7Fltn62uo9h37twpj8dTbXu+/fZbNW7cWM2bN1d0dLQGDBigN95447gzBmw2m89mTZK0YcMGrV69uk7x1dSAAQO0d+/eKj/f1157LaDXBRoyRoQB9SQzM1Nr1qzRe++9p+bNm3vLH330Ub377rsaO3as1q9fr+jo6Bqdr0ePHnr77bc1d+5cJSUlKSIiQr179z7uc4YNG6a3335bEyZM8O5W9Oijj6pt27Z1Xpuhtr766itvEqW0tFRvv/22VqxYoV//+tfeO3Y33nijcnNzdeWVV+quu+5S37591ahRIxUVFenjjz/W8OHD9etf//qY17j88suVkpKi++67T2VlZUpOTvbuGnneeedp9OjRJ4zzkUce0YoVK9S/f3/deeedOvPMM+VyubRt2zYtX75czz///DGHwG/ZskUpKSm68cYbNWDAALVt21a7d+/WX//6V82bN08DBw5U//79JUnp6elasmSJhg8frvvvv199+/bVgQMHtGrVKg0bNkyDBg3S0KFDNXv2bI0aNUq//e1vVVpaqlmzZlXpTPlbt27dNHLkSGVlZclut+uSSy7Rpk2blJWVpdjY2CrbhgMAgOqFcz/wvffe0w8//KAnn3yy2p0Ru3fvrmeeeUYvv/yyhg0bVu05mjVrpsTERC1dulSXXnqpWrZsqbi4OHXq1El/+MMfdOGFF+qiiy7S7373O3Xq1El79+7V1q1b9e677x73ZuPxLFy4UC+88IJGjRqlPn36KDY2VkVFRXrppZe0adMmPfTQQ4qKipJ0ZNrjhRdeqPPPP1/333+/Tj/9dO3cuVPLli3TCy+8oGbNmmnYsGF69NFH9fDDD2vAgAHasmWLHnnkEXXu3DmgNxjHjBmjOXPmKC0tTY899phOP/10vffee8rLy5Mk+nMITxYv1g+EhfXr15tGjRqZW2+9tdrjq1evNhEREWbSpEk1Pud//vMfc91115nmzZsbm81mKv6cK3YLeuqpp6p93hNPPGE6depkHA6HOfvss82LL77o3Z2nsmPtFvTGG2/41Ku43ol2nKlu18jY2Fhz7rnnmtmzZxuXy+VT/9ChQ2bWrFnmnHPOMU6n0zRt2tScddZZZvz48ebbb7/11qtu10hjjDlw4IC57777TGJiomnUqJFp27at+d3vfmd2795dpZ1Dhw6tNuaffvrJ3HnnnaZz586mUaNGpmXLliYpKclMmzbN7Nu375ht3b17t3nsscfMJZdcYtq3b2+ioqJMkyZNzLnnnmsee+wxs3///ir177rrLtOxY0fTqFEj07p1azN06FDzz3/+01vnlVdeMWeeeaZxOBzm1FNPNZmZmebll182ksx3333nrVebXSMLCgp86lW3I5HL5TKTJ082rVu3Nk6n01xwwQVm9erVJjY2tlavVwAAwlW49wOvvvpqExUVddwdFW+88UYTGRlpiouLq9010hhj/u///s+cd955xuFwVNm9+rvvvjNjx4417du3N40aNTKnnHKK6d+/v3nsscdO2IZj+frrr82UKVNM7969zSmnnGIiIyNNixYtzIABA8zChQurrT9ixAjTqlUrExUVZTp27Ghuuukmbx+3vLzc3H333aZ9+/bG6XSaXr16mT//+c9mzJgxVXYAPbrvdqxdI6vrA1f3+9y+fbu55pprTNOmTU2zZs3Mtddea5YvX24kmaVLl9bo5wGEEpsxxtRb1g0AEPQ+++wzJScnKzc3V6NGjbI6HAAAANTSjBkz9OCDD2r79u0nXOgfCDVMjQQAHNOKFSu0evVqJSUlKTo6Wl9++aWeeOIJnXHGGbrmmmusDg8AAAAn8Mwzz0iSzjrrLB06dEgfffSR/vjHPyotLY0kGMISiTCggXG73TreQE2bzVbrHXWAuoqJidEHH3yg7Oxs7d27V3FxcRoyZIgyMzOrbNcNAABODv1ABELjxo01Z84cbdu2TeXl5erYsaPuu+8+Pfjgg1aHBliCqZFAAzNw4ECtWrXqmMcTExO1bdu2+gsIAAAA9YJ+IAAEHokwoIHZsmWL9u7de8zjDodDPXr0qMeIAAAAUB/oBwJA4JEIAwAAgN8cPnxYGRkZys3NVXFxsdq2baubbrpJDz74oCIiIqwODwAAhDnWCAMAAIDfPPnkk3r++ee1YMECdevWTWvWrNHNN9+s2NhY3XXXXVaHBwAAwlytE2GffPKJnnrqKa1du1Y//vij3nnnHV199dXe48YYTZ8+XfPmzdPu3bt1/vnn69lnn1W3bt28dcrLy3X33Xdr8eLFOnDggC699FI999xzNd6xwuPx6IcfflCzZs1ks9lq2wQAABCmjDHau3ev2rVrx+ikAFm9erWGDx+uoUOHSpI6deqkxYsXa82aNTV6Pv08AABQFzXt59U6EfbLL7/onHPO0c0336xrr722yvGZM2dq9uzZmj9/vrp06aLHHntMl19+ubZs2aJmzZpJktLT0/Xuu+/qtddeU6tWrTRlyhQNGzZMa9eurdEuKD/88IM6dOhQ29ABAAAkSTt27GDL+AC58MIL9fzzz+ubb75Rly5d9OWXX+pvf/ubsrOzq61fXl6u8vJy7/fff/+9unbtWk/RAgCAUHOift5JrRFms9l8RoQZY9SuXTulp6frvvvuk3SkcxMfH68nn3xS48eP1549e3TKKado4cKFuuGGGyT9L7G1fPlypaSknPC6e/bsUfPmzbVjxw7FxMTUNXwAABBmysrK1KFDB/3888+KjY21OpyQZIzRAw88oCeffFJ2u11ut1uPP/64pk6dWm39jIwMTZ8+vUo5/TwAAFAbNe3n+XWNsO+++07FxcUaPHiwt8zhcGjAgAH67LPPNH78eK1du1aHDh3yqdOuXTt1795dn332WbWJsKPvFFbspBITE0MHCQAA1BpT7gJnyZIlysnJ0aJFi9StWzetX79e6enpateuncaMGVOl/tSpUzV58mTv9xWdWPp5AACgLk7Uz/NrIqy4uFiSFB8f71MeHx+vwsJCb52oqCi1aNGiSp2K5x8tMzOz2juFAAAAaFjuuece3X///brxxhslST169FBhYaEyMzOrTYQ5HA45HI76DhMAAISpgKwSe3T2zRhzwozc8epMnTpVe/bs8T527Njht1gBAADgP/v376+yQK3dbpfH47EoIgAAgP/x64iwNm3aSDoy6qtt27be8l27dnlHibVp00YHDx7U7t27fUaF7dq1S/3796/2vNwpBAAACA5XXXWVHn/8cXXs2FHdunXTF198odmzZ2vs2LFWhwYAAODfEWGdO3dWmzZttGLFCm/ZwYMHtWrVKm+SKykpSY0aNfKp8+OPP+qrr746ZiIMAAAAweHpp5/WddddpwkTJujss8/W3XffrfHjx+vRRx+1OjQAAIDajwjbt2+ftm7d6v3+u+++0/r169WyZUt17NhR6enpmjFjhs444wydccYZmjFjhho3bqxRo0ZJkmJjYzVu3DhNmTJFrVq1UsuWLXX33XerR48euuyyy/zXMgAAANS7Zs2aKTs7W9nZ2VaHAgAAUEWtE2Fr1qzRoEGDvN9X7PIzZswYzZ8/X/fee68OHDigCRMmaPfu3Tr//PP1wQcfqFmzZt7nzJkzR5GRkbr++ut14MABXXrppZo/f77sdrsfmgQAAAAAAABUZTPGGKuDqK2ysjLFxsZqz549bKsNAABqjD5Ew8fvCAAA1EVN+xAB2TUSAAAAAAAAaGhIhAEAAAAAACAskAgDAAAAAABAWCARBgAAAABBLD8/XyNGjFB+fr7VoQBAg0ciDAAAAACClMvlUlZWlnbu3KmsrCy5XC6rQwKABo1EGAAAAAAEqZycHJWWlkqSSktLlZuba3FEANCwRVodAAAcjzGmVnc2jTEqLy+XJDkcDtlstho9z+l01rguAABAQ1BUVKTc3FwZYyQd6Qfl5uYqJSVFCQkJFkcHAA0TiTAADZrL5VJKSkrAr5OXl6fo6OiAXwcAAMAfjDGaM2fOMctnzZrFTT4AqAZTIwEAAAAgyBQWFqqgoEBut9un3O12q6CgQIWFhRZFBgANGyPCADRoTqdTeXl5Na7vcrk0fPhwSdLSpUvldDprfB0AAIBgkZiYqD59+mjdunU+yTC73a6kpCQlJiZaGB0ANFwkwgA0aDabrc5TFp1OJ9MdAQBASLLZbJo0aZJGjx5dbTnTIgGgekyNBAAAAIAglJCQoNTUVG/Sy2azKTU1Ve3bt7c4MgBouEiEAQAAAECQSktLU6tWrSRJcXFxSk1NtTgiAGjYSIQBAAAAQJByOp2aMmWK4uPjNXnyZNY9BYATYI0wAAAAAAhiycnJSk5OtjoMAAgKjAgDAAAAAABAWCARBgAAAAAAgLBAIgwAAAAAAABhgUQYAAAAAAAAwgKJMAAAAAAAAIQFEmEAAAAAAAAICyTCAAAAAAAAEBZIhAEAAAAAACAskAgDAAAAAABAWCARBgAAAAAAgLBAIgwAAAAAAABhgUQYAAAAAAAAwgKJMAAAAAAAAISFSKsDQOAZY+RyuWpct7y8XJLkcDhks9lqfB2n01mr+gAAAAAAAPWJRFgYcLlcSklJCfh18vLyFB0dHfDrAAAAAAAA1AVTIwEAAAAAABAWGBEWBpxOp/Ly8mpU1+Vyafjw4ZKkpUuXyul01uo6AAAAAAAADRWJsDBgs9nqNGXR6XQy1RF+V5s16+qi8rkDeR3WxAMAAACA4EMiDEC9qq816yR5RzcGAmviAQAAAEDwYY0wAAAAAAAAhAVGhAGwzK/OnaDIiEZ+PacxRm7PYUmSPSLSr9MXD3sOadn65/x2PgAAAABA/SIRBsAykRGNFGmP8vt5G8nh93MCAAAAAIIfUyMBAAAAAAAQFkiEAQAAAAAAICyQCAMAAAAAAEBYIBEGAAAAAACAsEAiDAAAAAAAAGGBRBgAAAAAAADCAokwAAAAAAAAhAUSYQAAAAAAAAgLJMIAAAAAAAAQFkiEAQAAAAAAICyQCAMAAAAAAEBYIBEGAAAAAACAsEAiDAAAAAAAAGGBRBgAAAAAAADCAokwAAAA+NX333+vtLQ0tWrVSo0bN9a5556rtWvXWh0WAACAIq0OAAAAAKFj9+7dSk5O1qBBg/Tee++pdevW+te//qXmzZtbHRoAAACJMAAAAPjPk08+qQ4dOujVV1/1lnXq1Mm6gAAAACohEQagXhljvF8fdh+yMJLaqxxv5XYAAP5n2bJlSklJ0YgRI7Rq1Sq1b99eEyZM0K233lpt/fLycpWXl3u/Lysrq69QAQBAGCIRBqBeVf6ws+zL5yyM5OSUl5ercePGVocBAA3Ov//9b82dO1eTJ0/WAw88oH/84x+688475XA49Jvf/KZK/czMTE2fPt2CSAEAQDhisXwAAAD4jcfjUa9evTRjxgydd955Gj9+vG699VbNnTu32vpTp07Vnj17vI8dO3bUc8QAACCcMCIMQL1yOBzer391zgRF2htZGE3tHHYf8o5iq9wOAMD/tG3bVl27dvUpO/vss/XWW29VW9/hcPCeCgAA6g2JMAD1ymazeb+OtDdSpD3KwmjqrnI7AAD/k5ycrC1btviUffPNN0pMTLQoIiD05efnKzs7W+np6UpOTrY6HABo0JgaCQAAAL+ZNGmSPv/8c82YMUNbt27VokWLNG/ePE2cONHq0ICQ5HK5lJWVpZ07dyorK0sul8vqkACgQSMRBgAAAL/p06eP3nnnHS1evFjdu3fXo48+quzsbKWmplodGhCScnJyVFpaKkkqLS1Vbm6uxREBQMPG1EgAAAD41bBhwzRs2DCrwwBCXlFRkXJzc2WMkSQZY5Sbm6uUlBQlJCRYHB0ANEx+HxF2+PBhPfjgg+rcubOio6N16qmn6pFHHpHH4/HWMcYoIyND7dq1U3R0tAYOHKhNmzb5OxQAAAAACEnGGM2ZM+eY5RXJMQCAL78nwp588kk9//zzeuaZZ7R582bNnDlTTz31lJ5++mlvnZkzZ2r27Nl65plnVFBQoDZt2ujyyy/X3r17/R0OAAAAAIScwsJCFRQUyO12+5S73W4VFBSosLDQosgAoGHzeyJs9erVGj58uIYOHapOnTrpuuuu0+DBg7VmzRpJR+5QZGdna9q0abrmmmvUvXt3LViwQPv379eiRYv8HQ4AAAAAhJzExET16dNHdrvdp9xut6tv377s1AoAx+D3RNiFF16oDz/8UN98840k6csvv9Tf/vY3XXnllZKk7777TsXFxRo8eLD3OQ6HQwMGDNBnn31W7TnLy8tVVlbm8wAAAACAcGWz2TRp0qRjlttsNguiAoCGz++JsPvuu08jR47UWWedpUaNGum8885Tenq6Ro4cKUkqLi6WJMXHx/s8Lz4+3nvsaJmZmYqNjfU+OnTo4O+wAQAAACCoJCQkKDU11Zv0stlsSk1NVfv27S2ODAAaLr8nwpYsWaKcnBwtWrRI69at04IFCzRr1iwtWLDAp97RdyiMMce8azF16lTt2bPH+9ixY4e/wwYAAACAoJOWlqZWrVpJkuLi4pSammpxRADQsEX6+4T33HOP7r//ft14442SpB49eqiwsFCZmZkaM2aM2rRpI+nIyLC2bdt6n7dr164qo8QqOBwOORwOf4cKAAAAAEHN6XRqypQpys7OVnp6upxOp9UhAUCD5vcRYfv371dEhO9p7Xa7PB6PJKlz585q06aNVqxY4T1+8OBBrVq1Sv379/d3OAAAAAAQ0pKTk/XGG28oOTnZ6lAAoMHz+4iwq666So8//rg6duyobt266YsvvtDs2bM1duxYSUemRKanp2vGjBk644wzdMYZZ2jGjBlq3LixRo0a5e9wAAAAAAAAAEkBSIQ9/fTT+v3vf68JEyZo165dateuncaPH6+HHnrIW+fee+/VgQMHNGHCBO3evVvnn3++PvjgAzVr1szf4QAAAAAAAACSApAIa9asmbKzs5WdnX3MOjabTRkZGcrIyPD35QEAAAAAAIBq+X2NMAAAAAAAAKAhIhEGAAAAAACAsEAiDAAAAAAAAGGBRBgAAAAAAADCAokwAAAAAAAAhAUSYQAAAAAAAAgLJMIAAAAAAAAQFkiEAQAAAAAAICyQCAMAAAAAAEBYIBEGAAAAAACAsEAiDAAAAAAAAGGBRBgAAAAAAADCAokwAAAAAAAAhAUSYQAAAAAAAAgLkVYHgNozxsjlcgXk3JXPG6hrVHA6nbLZbAG9BgAAAAAAQAUSYUHI5XIpJSUl4NcZPnx4QM+fl5en6OjogF4DAAAAAACgAlMjAQAAAAAAEBYYERbknr34Zznsxm/nM0Y66DnydVSE5O+Zi+VumyZ+0ty/JwUAAAAAAKgBEmFBzmE3ctr9e87ATlb0X9IOAAAAAACgNpgaCQAAAAAAgLBAIgwAAAAAAABhgUQYAAAAAAAAwgKJMAAAAAAAAIQFEmEAAAAAAAAICyTCAAAAAAAAEBZIhAEAAAAAACAskAgDAAAAAABAWIi0OgAA4euw55Dfz2mMkdtzWJJkj4iUzWbz27kDES8AAAAAoP6QCANgmWXrn7M6BAAAAABAGGFqJAAAAAAAAMICI8IA1Cun06m8vLyAnd/lcmn48OGSpKVLl8rpdAbkOoE6LwAAAAAgcEiEAahXNptN0dHR9XItp9NZb9cCAAAAADR8TI0EAAAAAABAWCARBgAAAAAAgLBAIgwAAAAAAABhgUQYAAAAAAAAwgKJMAAAAAAAAIQFEmEAAAAAAAAICyTCAAAAAAAAEBZIhAEAAAAAACAskAgDgCCVn5+vESNGKD8/3+pQAAAA4Ef084DAIREGAEHI5XIpKytLO3fuVFZWllwul9UhAQAAwA/o5wGBRSIMAIJQTk6OSktLJUmlpaXKzc21OCIAqF5mZqZsNpvS09OtDgUAggL9PCCwSIQBQJApKipSbm6ujDGSJGOMcnNzVVRUZHFkAOCroKBA8+bNU8+ePa0OBWGIqWUIRvTzgMAjEQYAQcQYozlz5hyzvKLTBABW27dvn1JTU/Xiiy+qRYsWVoeDMMPUMgQj+nlA/SARBgBBpLCwUAUFBXK73T7lbrdbBQUFKiwstCgyAPA1ceJEDR06VJdddtlx65WXl6usrMznAZwsppYhGNHPA+oHiTAACCKJiYnq06eP7Ha7T7ndblffvn2VmJhoUWQA8D+vvfaa1q1bp8zMzBPWzczMVGxsrPfRoUOHeogQoYypZQhW9POA+kEiDACCiM1m06RJk45ZbrPZLIgKAP5nx44duuuuu5STkyOn03nC+lOnTtWePXu8jx07dtRDlAhVTC1DMKOfB9QPEmEAEGQSEhKUmprq7QzZbDalpqaqffv2FkcGANLatWu1a9cuJSUlKTIyUpGRkVq1apX++Mc/KjIyssqUH4fDoZiYGJ8HUFdMLUOwo58HBF6k1QGg9irfySp3H6diA1Q5Xu7IAXWXlpam5cuXq6SkRHFxcUpNTbU6JACQJF166aXauHGjT9nNN9+ss846S/fdd1+VKT+AP1VMLVu3bp1PMsxutyspKYmpZQgK9POAwCIRFoTKy8u9X0/8JHh3YSovL1fjxo2tDgMISk6nU1OmTFF2drbS09NrNP0IAOpDs2bN1L17d5+yJk2aqFWrVlXKAX+rmEI2evToasuZWoZgQD8PCCymRgJAkEpOTtYbb7yh5ORkq0MBAKDBCMepZfn5+RoxYoTy8/OtDgV+Qj8PCBxGhAUhh8Ph/frZi3fLEUQzDMrd/xvFVrkdAAAgdK1cudLqEBBmwmlqmcvlUlZWlkpKSpSVlaWkpCRGEAHAcTAiLAhVHtLtsEvOIHpUTtoxNB0AAACBUDG1LD4+XpMnTw7pxFBOTo5KS0slSaWlpcrNzbU4IgBo2BgRBgAAACDkJCcnh/y0sqKiIuXm5no3oTLGKDc3VykpKUpISLA4OgBomBgRBgAAAABBxhijOXPmHLOcHdoBoHokwgAAAAAgyBQWFqqgoEBut9un3O12q6CgQIWFhRZFBgANG4kwAAAAAAgyiYmJ6tOnj+x2352z7Ha7+vbtq8TERIsiA4CGjUQYAAAAAAQZm82mSZMmVTsFctKkSWxMBQDHQCIMAAAAAIJQQkKCunXr5lPWrVs3tW/f3qKIAKDhIxEGAAAAAEGoqKhIX3/9tU/Z119/raKiIosiAoCGj0QYAAAAAAQZdo0EgLoJSCLs+++/V1pamlq1aqXGjRvr3HPP1dq1a73HjTHKyMhQu3btFB0drYEDB2rTpk2BCAUAAAAAQg67RgJA3fg9EbZ7924lJyerUaNGeu+99/T1118rKytLzZs399aZOXOmZs+erWeeeUYFBQVq06aNLr/8cu3du9ff4QAAAABAyGHXSACoG78nwp588kl16NBBr776qvr27atOnTrp0ksv1WmnnSbpyGiw7OxsTZs2Tddcc426d++uBQsWaP/+/Vq0aJG/wwEAAACAkFOxa+Sxytk1Mrjl5+drxIgRys/PtzqUgAuntqJh8HsibNmyZerdu7dGjBih1q1b67zzztOLL77oPf7dd9+puLhYgwcP9pY5HA4NGDBAn332WbXnLC8vV1lZmc8DAAAAAMJZQkKCUlNTvUkvm82m1NRUdo0Mci6XS1lZWdq5c6eysrLkcrmsDilgwqmtaDj8ngj797//rblz5+qMM85QXl6ebrvtNt15553605/+JEkqLi6WJMXHx/s8Lz4+3nvsaJmZmYqNjfU+OnTo4O+wAQAAACDoVKzNLElxcXFKTU21OCKcrJycHJWWlkqSSktLlZuba3FEgRNObUXD4fdEmMfjUa9evTRjxgydd955Gj9+vG699VbNnTvXp97RQ3WNMcccvjt16lTt2bPH+9ixY4e/wwYAAACAoON0OjVlyhTFx8dr8uTJcjqdVoeEk1BUVKTc3Fzvrp/GGOXm5qqoqMjiyPwvnNqKhsXvibC2bduqa9euPmVnn322tm/fLklq06aNJFUZ/bVr164qo8QqOBwOxcTE+DwAAAAAAFJycrLeeOMNJScnWx0KToIxRnPmzDlmeUXCKBSEU1vR8Pg9EZacnKwtW7b4lH3zzTfeXUs6d+6sNm3aaMWKFd7jBw8e1KpVq9S/f39/hwMAAAAAQINXWFiogoICud1un3K3262CggIVFhZaFJn/hVNb0fD4PRE2adIkff7555oxY4a2bt2qRYsWad68eZo4caKkI1Mi09PTNWPGDL3zzjv66quvdNNNN6lx48YaNWqUv8MBAAAAAKDBS0xMVJ8+fRQR4fsxPSIiQn379vUOLgkFFW09enkkm80Wcm1Fw+P3RFifPn30zjvvaPHixerevbseffRRZWdn+yzaeO+99yo9PV0TJkxQ79699f333+uDDz5Qs2bN/B0OAAAAAAANns1m06RJk6pMCzTGaNKkScdcUzsY2Ww2jRw5stq2jhw5MqTaioYnMhAnHTZsmIYNG3bM4zabTRkZGcrIyAjE5QEAAAAACAk2my3k1swyxmjx4sVV2maz2bRo0SL16tWLZBgCxu8jwgAAAAAAQO1ULBR/9NRIm80WcgvIV6wRVt2IMNYIQ6CRCAMAAACAIJafn68RI0YoPz/f6lBwEsJpAfmKNcLsdrtPud1uZ40wBByJMAAIUnR6AQCAy+VSVlaWdu7cqaysLLlcLqtDQh2FU3KoYj20Y5UzLRKBRCIMAIIQnV4AACBJOTk5Ki0tlSSVlpYqNzfX4ohQV+GWHEpISFBqaqq3XTabTampqWrfvr3FkSHUkQgDgCBEpxcAABQVFSk3N9e7zpIxRrm5uSoqKrI4MtRVuCWH0tLS1KpVK0lSXFycUlNTLY4I4YBEGAAEGTq9AACgYmH1Y5WH0sLq4ea6667zSYRde+21FkcUOE6nU1deeaUiIiI0ZMgQOZ1Oq0NCGCARBgBBhE4vAACQwmth9XDz5ptvyuPxSJI8Ho/eeustiyMKHJfLpeXLl8vj8Wj58uUs94F6QSIMAIIInV4AACCF18Lq4aRi5H9loTzyn+U+YAUSYQAQROj0AgAAKfwWVg8Hxxrh7/F4QnLkP8t9wCokwgAgiNDpBQAAFcJtYfVQVzHyv2JaZAWPxxNyI/9Z7gNWIhEGAEEmISFBN9xwg0/ZDTfcQKcXAIAwxK57oSMxMVE9evSo9ljPnj1DauQ/y33ASiTCAAAAACBIOZ1OTZkyRfHx8Zo8eTK77gW5cBndX7Hcx9HttdlsLPeBgCMRBgBBpqioSEuWLPEpW7JkCespAAAABLHCwkJt2LCh2mMbNmwIqVFSNptNI0eOrDIF0hijkSNHhk1CENYgEQYAQYT1FAAAQGUul0tZWVnauXOnsrKy5HK5rA4JdVQxSioiwvdjeihuimSM0eLFi6sdEbZo0SL6tAgoEmEAEERYTwEATswYowMHDtT4sX//fu3evVu7d+/W/v37a/VcPqzBajk5OSotLZUklZaWKjc31+KIUFfH2vwoFDdFqujTVjcijD4tAi3S6gAAADVXcadw3bp1Pskwu92upKSkkLpTCAB15XK5lJKSUi/XysvLU3R0dL1cCzhaUVGRcnNzvckEY4xyc3OVkpKihIQEi6NDXVTsBPqnP/3JWxaKO4HSp4WVGBEGAEGk4o7gscpD6U4hAAA4NpZLCF3XXXedt09ns9l07bXXWhyR/9GnhZUYEQYAQabiTuHChQtljJHNZgvJO4UAUFdOp1N5eXk1ru9yuTR8+HBJ0tKlS2u16x479MEqFVPLjlZ5uYROnTrVf2A4aa+99prPKL8lS5Zo/PjxFkdVM8aYGq9T16pVK11//fXe9tpsNl1//fVq2bKlDhw4cMLnO51OEmaoExJhABCE0tLStHz5cpWUlCguLk6pqalWhwQADYbNZqvzdEWn08lURwQFppaFpqKiIi1evNinbNGiRRo6dGhQTHc9manpxhgtWrRIixYtqlF9pqajrpgaGeTK3Ta53PLb48Bhac/BI48Dh/133opHuZuMPeAPTqdTU6ZMUXx8vCZPnsyIBAAAjvLSSy9p4MCBeumll6wOJSCYWhZ6jDF64oknql1AvrpyAHXDiLAgN/GT5laHAAAAADQoP//8s3JycuTxeJSTk6PrrrtOzZs3tzosv0tISNANN9zgM4LmhhtuYLmEILVt2zZt2LCh2mMbNmzQtm3b1Llz53qOqnaYmo5gQCIMAIKQy+VSVlaWSkpKlJWVpaSkJDoDAAD817Rp0+TxeCRJHo9HDz74oJ555hmLowKO70QjvoJhRBhT0xEMSIQFodpm2WvjZDLytcWHdqDucnJyVFpaKkkqLS1Vbm6uxo0bZ3FUAABYb82aNdq4caNP2YYNG7RmzRr17t3boqgCo6ioSEuWLPEpW7JkSdCsJwVfJ5rOynRXwD9IhAWhk8my1wYZeaBhKioqUm5urs9uQrm5uUpJSaHTCwAIax6PRxkZGdUey8jI0LJlyxQRERrLJBtjNGfOnCqjhDwej+bMmaNZs2aROAkynTp1Us+ePaudHnnOOeewCyjgJ6HxXwAAwkRFp/dY5cEwZB4AgEBZvXq1ysrKqj1WVlam1atX13NEgVNYWKiCggLvFNAKHo9HBQUFKiwstCgy1JXNZtP9999/zHISm4B/kAgDgCBS0emtvE26JLndbjq9AICw169fP8XExFR7LDY2Vv369avniAInMTFRPXr0qPZYz549lZiYWM8R4XiMMTpw4MAJH61atdKIESN8njtixAi1bNmyRs/npihwYkyNBIAgkpiYqD59+mjNmjU+HR2bzaY+ffrQ6QUAhLWIiAhlZGRo8uTJVY5Nnz49ZKZFVmCEUPBwuVxKSUmp03Nff/11vf766zWqm5eXx/I2wAmE1n8CAAhxNptNI0eOrHK3zxijkSNH0iEGAIS93r17Vxkp1bNnT/Xq1cuiiAKjsLCw2rWkpCObAzBKHACqx4gwAAgixhgtXrxYNputyoiwRYsWqVevXiTDAABh7/HHH9fVV18tj8ejiIgIPfbYY1aH5HcVo8TXrl3rs06Y3W5XUlISo8QbGKfTqby8vBrVdblcGj58uCRp6dKlcjqdtboOgONjRBgABJGKNcKqGxHGGmEAABzRvHlzpaWlKSIiQmlpaWrevLnVIfmdzWbTpEmTqtwAO1Y5rGWz2RQdHV2jR+VkltPprPHzoqOj+b0DNUAiDACCSMXdX7vd7lNut9vVt29f7v4CAPBft9xyi1auXKlbbrnF6lACJiEhQampqd7kh81mU2pqqtq3b29xZADQcJEIA4AgUnGX91jl3AUEACC8pKWlqVWrVpKkuLg4paamWhwRADRsJMIAIMhw9xcAAFRwOp2aMmWK4uPjNXnyZNaIAoATIBEGAEGIu78AGqrMzEz16dNHzZo1U+vWrXX11Vdry5YtVocFhLTk5GS98cYbSk5OtjoUAGjw2DUSAIJQxd3f7Oxspaenc/cXQIOxatUqTZw4UX369NHhw4c1bdo0DR48WF9//bWaNGlidXgIUsYYuVyuWtUvLy+XJDkcjlotHeB0OllqAABCGIkwAAAA+M3777/v8/2rr76q1q1ba+3atbr44ostigrBzuVyKSUlpV6ulZeXp+jo6Hq5FgCg/jE1EgCCkMvlUlZWlnbu3KmsrKxa3SUHgPq0Z88eSVLLli0tjgQAAIARYQAQlHJyclRaWipJKi0tVW5ursaNG2dxVADgyxijyZMn68ILL1T37t2rrVNeXu6dwiZJZWVl9RUegojT6VReXl6N67tcLg0fPlyStHTp0lotIcByAwAQ2kiEAUCQKSoqUm5urowxko580MzNzVVKSooSEhIsjg4A/uf222/Xhg0b9Le//e2YdTIzMzV9+vR6jArByGaz1Xm6otPpZKojAMCLqZEAEESMMZozZ448Ho9Pudvt1pw5c7zJMQCw2h133KFly5bp448/Pm6SfurUqdqzZ4/3sWPHjnqMEggN+fn5GjFihPLz860OBQAaPEaEAUAQKSwsVEFBQZVyY4wKCgpUWFioTp061X9gAPBfxhjdcccdeuedd7Ry5Up17tz5uPUdDoccDkc9RRd66ms3RXZSbLhcLpcyMzNVVlamzMxMvfnmm0zvBIDjIBEGAEGkY8eOiomJqXYNnZiYGHXs2NGCqADgfyZOnKhFixZp6dKlatasmYqLiyVJsbGxTE8LgPraTZGdFBuu+fPne/sFZWVlWrBggcaPH29xVADQcDE1EgCCyPbt24+5kHRZWZm2b99ezxEBgK+5c+dqz549GjhwoNq2bet9LFmyxOrQgJBTVFSkxYsX+5QtXrxYRUVFFkUEAA0fI8IAIIgwIgxAQ8dahfWrvnZTZKpdw2OM0RNPPFHlb87j8eiJJ57Q008/zXRWAKgGiTAACCI1GRHGGmEAED7YTTF8bdu2TRs2bKj22IYNG7Rt27YTrtEHAOGIqZEAEEQSExPVp0+fKnd4bTab+vbtq8TERIsiAwAAAICGj0QYAAQRm82mSZMmKSLC9+3bbrdr0qRJTIEAACBMJCYmqnHjxtUea9y4MTfHAOAYSIQBQJBJSEhQamqqN+lls9mUmpqq9u3bWxwZAACoL4WFhdq/f3+1x/bv36/CwsJ6jggAggOJMAAIQmlpaWrVqpUkKS4uTqmpqRZHBAAAAAANH4vlA0ADYYyRy+Wqcd3x48dr3rx5mjhxoowxOnDgQI2e63Q6mUIJAECQ69Spk3r27FntgvnnnHMOm+cAwDGQCAOABsLlciklJaXWz8vIyKhV/by8PHYJAwAgyNlsNt1///1KTU2VMaZKOTe9AKB6TI0EAAAAgCCUkJCgrl27+pR169aNdUMB4DgYEQYADYTT6VReXl6N6rpcLg0fPlyStHTpUjmdzlpdBwAABL+ioiJt3rzZp2zz5s0qKipSQkKCRVEBQMNGIgwAGgibzVanKYtOp5OpjgAAhBljjObMmXPM8lmzZjE9EgCqQSIMQINWmwXkJfnUrc3zWEAeAAAEk8LCQhUUFFQp93g8KigoUGFhIQvmA0A1SIQBaNDquoC8JO/UwZpgAXkAABBMEhMT1aNHD23cuLHKsZ49eyoxMdGCqACg4WOxfAAAAAAIQoxmB4DaC9sRYbWdbmWMUXl5uSTJ4XDU+J8O062Ak1ObBeSlI3+rn376qebNm6eJEyeqX79+Nb4OAABAsCgsLNSGDRuqPbZhwwamRgLAMYRtIuxkplvVBtOtgJNT2wXkXS6Xnn76aZWVlWn27Nl68803SXIBAICQk5iYqD59+mjt2rXyeDzecrvdrqSkJKZGAsAxhG0iDEBomj9/vsrKyiRJZWVlWrBggcaPH29xVAAAAP5ls9k0adIkjR49utryYJiVwiwdAFYI20RYbadbuVwu78LbS5curfEIE0aiAPWnqKhIixcv9ilbvHixhg4dqoSEBIuiAgAACIyEhASlpqZq4cKFMsbIZrMpNTVV7du3tzq0GmGWDgArhO1i+RXTrWr6qJzQcjqdNX4edx6A+mGM0RNPPCFjjE+5x+OpthwAACAUpKWlqVWrVpKkuLg4paamWhwRADRsAR8RlpmZqQceeEB33XWXsrOzJR35wDp9+nTNmzdPu3fv1vnnn69nn31W3bp1C3Q4AELUtm3bjrtg7LZt29S5c+d6jgoAACCwnE6npkyZouzsbKWnpwfVjBRm6QCwQkATYQUFBZo3b5569uzpUz5z5kzNnj1b8+fPV5cuXfTYY4/p8ssv15YtW9SsWbNAhgQAAAAAIWXz5s366aeftHnzZiUnJ1sdTo3VdlOkyipm6QBAbQVsauS+ffuUmpqqF198US1atPCWG2OUnZ2tadOm6ZprrlH37t21YMEC7d+/X4sWLQpUOABCXKdOndSjR49qj/Xs2ZPtwwEAQEj6+eeflZOTI4/Ho5ycHP38889WhwQADVrAEmETJ07U0KFDddlll/mUf/fddyouLtbgwYO9ZQ6HQwMGDNBnn31W7bnKy8tVVlbm8wCAymw2m6ZOnVplXb5jlQMAAISCadOmyePxSDqyNuqDDz5ocUQA0LAFJBH22muvad26dcrMzKxyrLi4WJIUHx/vUx4fH+89drTMzEzFxsZ6Hx06dPB/0ACCXkJCgkaOHOlTNmrUqKDZOQkAAKA21qxZo40bN/qUbdiwQWvWrLEoIgBo+Py+RtiOHTt011136YMPPjjuooRHj86o2O63OlOnTtXkyZO935eVlZEMA1Ctm266Se+++6727t2rmJgYjRkzxuqQAAAA/M7j8SgjI6PaYxkZGVq2bJkiIgI2AQhAEDPGyOVy1ap+eXl5ACM6wuFw1Gomj9PprNPMH78nwtauXatdu3YpKSnJW+Z2u/XJJ5/omWee0ZYtWyQdGRnWtm1bb51du3ZVGSVWweFwyOFw+DtUACHI6XTqgQceCMqdkwAAAGpq9erVx1wypqysTKtXrw6qhfMB1B+Xy6WUlBSrwzhpeXl5ddo0w++3CC699FJt3LhR69ev9z569+6t1NRUrV+/XqeeeqratGmjFStWeJ9z8OBBrVq1Sv379/d3OAAAAAAQcvr166emTZtWe6xp06bq169fPUcEAMHB7yPCmjVrpu7du/uUNWnSRK1atfKWp6ena8aMGTrjjDN0xhlnaMaMGWrcuLFGjRrl73AAhBmXy6WsrCyVlJQoKytLSUlJjAoDAAAhx2azqX379t4ZN5W1b9+ejYIA1MjYcS41anT8OsZIhw8HPpbISOlEb12HDkmvvHxyn+/8ngiriXvvvVcHDhzQhAkTtHv3bp1//vn64IMP1KxZMyvCARBCcnJyVFpaKkkqLS1Vbm6uxo0bZ3FUAAAA/lVYWFhtEkyStmzZosLCQnXq1Kl+gwKCmMfj0Z49e2pcv77WzZJqt3ZWbGxsrdYHbNRIJ0yESVJUVI1P2eDVSyJs5cqVPt/bbDZlZGQcc3FHAKiLoqIi5ebmyhgj6cg/p9zcXKWkpCghIcHi6AAAAPwnMTFRffr00Zo1a7x9H0mKiIhQ7969lZiYaGF0QPDZs2ePhg8fbnUYJ23p0qVq0aKF1WE0aGwjAiAkGGM0Z86cY5ZX7iACAAAEO5vNpkmTJlUZ+REREaFJkyYxNRIAjsGSqZEA4G+FhYUqKCioUu52u1VQUMD0AAAAEHISEhLUtWtXbdy40VvWtWtXtW/f3sKogODkcDi8X/fr1092u/249Y0x8ng8gQ5L0pEE9/GS2263W6tXr5bk2w5Uj0QYgJBQMT1g3bp1crvd3nK73a6kpCSmBwBAEDPGyOVyBez8lc8dyOs4nc4TjtIJp7bi5BUVFWnTpk0+ZZs2bVJRUZEly0Lw+kUwq/w7j4qKOmEirCGp/PmH1+6JkQgDEBIqpgeMHj262nL+IQBA8HK5XEpJSamXawVyfZi8vDxFR0cft044tRUnp2L5h+r6OHPmzNGsWbPqvf/D6xdAMGCNMAAhIyEhQampqd5On81mU2pqKtMDAABAyKlYFqLySBDJd1kIAEBVjAgDEFLS0tK0fPlylZSUKC4uTqmpqVaHBADwo196pUoRfu7CGiN5Dh/5OiJS8ucoGs9hNVmXW6enPnvxz3LY/bvZizHSwf8uaRMV4d+mlrttmvhJc/+dEMfV0JeF+NW5ExQZ0civ5zTGyP3fv1V7RKRfR7wd9hzSsvXP+e18ABouEmEAQorT6dSUKVOUnZ2t9PR0OZ1Oq0MCAPhTRKRk9++H6yOiAnDOk+OwGzkDsERN4CZ8sUNzfWroy0JERjRSpN3/f1eNxELgAE4OiTAAISc5OVnJyclWhwEAABBQCQkJuvbaa/X66697y6699lqWhYBfBXIThPraAEFiEwT8D4kwAAAAAAhS1e0aCfhTfW2CEMgNECQ2QcD/hEwijK16AQAAgODBKJOTt2bNmiqJr6+++kpr1qxR7969LYkJABq6kEmEsVUvAAAAEDwYZXJyPB6PMjIyqj2WkZGhZcuWKSIion6DCiPhmsh9auDdcvhx7TdjjA56DkmSoiIa+T2pXO4+qHtWzvLrORH8QiYRBgAAAADhYvXq1SorK6v2WFlZmVavXs2aqQEUrolchz1Kjkj/boLgZAME1LOQTISF07baAAAAQLBzX+X27ycTI8n936/tkvw9c/GwZH83AFt61sIFF1wgm80mY6ru1mmz2XTBBRdYEBUANHwhmQgLp221AQAAgKAXKf9/MgnEx4EGpLCwsNokmHRkullhYaFOPfXUeo4qPA1sHye7HwdKGGPk+e+vNsImv08XdBujld+X+PWcQDAJzUQYAAAAAISw9evXn/A4ibD6YbfZFBnhz2RVgDdf8AT29EBDx+qJAAAAABBkfvWrX53UcQAIV4wIAwAAAIAgU1RUdMLjnTp1qp9g/qvyVM3D7kP1eu2TVTneY005BRAaSIQBAAAAQJBJTExUnz59VFBQUOVY3759lZiYWO8xlZeXe79e9uVz9X59fykvL1fjxo2tDgNAgIRMIswnax9kdx/E3QcAAAAAtWCz2TRy5MhqE2EjR470+wLrABAqQiYRVvnuQ5MvFlkYycnh7gMAAACAEzHGaPHixdUeW7RokXr16lXvyTCHw+H9+lfnTFCkPXi27jzsPuQdxVa5HQBCT8gkwgAAAAAgXBQWFlY7GkySCgoKVFhYWO9rhFVOvEXaGynSHlWv1/cXRtMBoS1kEmGVs/a/nDdKCqK7D3If8o5i4+4DAAAAgBPp0KGDIiIi5PF4qhyLiIhQhw4dLIgKABq+kEmE+WTt7Y2CKxFWCXcfAAAAAJzI559/Xm0STJI8Ho8+//xzJScn13NUANDwhUwiDAAAAKEpnDZFqlyn3B2QiAKmcrxsAFV3xhi5XK4T1qu8RvKxjh84cOC4dZxOJzfiAYQdEmEAAADwu+eee05PPfWUfvzxR3Xr1k3Z2dm66KKL6nSucNoUqXJbJ37SItAhBQwbQNWdy+VSSkrKSZ8nIyPjhHXy8vIUHR190tcCgGASYXUAAAAACC1LlixRenq6pk2bpi+++EIXXXSRhgwZou3bt1sdGgAACHOMCAMAAIBfzZ49W+PGjdMtt9wiScrOzlZeXp7mzp2rzMzMWp8vnDZFqlzn2Yt3y2EPWGR+V+7+3yg2NoCqO6fTqby8vBrXv/322/Xtt996vz/rrLP0hz/8ocbXAoBwE5qJMM9h/5/TmP+dNyJS8udc+kDECwAAYIGDBw9q7dq1uv/++33KBw8erM8++6xO5wynTZEq13HYJWcQJcIqY92purPZbLWarvj444/r+uuv934/c+ZMpjsCwHGEZCKsybpcq0MAAAAISyUlJXK73YqPj/cpj4+PV3FxcZX65eXlPutilZWVBTxGIJTExsZ6vx41apSaN29uXTAAEARYIwwAAAB+d/SIIGNMtaOEMjMzFRsb63106NChvkIEQs6YMWOsDgEAGryQGRFW27n0teVyuTR8+HBJ0tKlSwM2n555+sDJy8/PV3Z2ttLT05WcnGx1OAAQVuLi4mS326uM/tq1a1eVUWKSNHXqVE2ePNn7fVlZGckwAAAQMCGTCKvtXPqT4XQ6mXcPNFAul0tZWVkqKSlRVlaWkpKSSDADQD2KiopSUlKSVqxYoV//+tfe8hUrVnhvKlbmcDhYWB0AANSbkEmEAYAk5eTkqLS0VJJUWlqq3NxcjRs3zuKoACC8TJ48WaNHj1bv3r3Vr18/zZs3T9u3b9dtt91mdWhAvTPGyOVyBez8lc8dyOs4nU42QQAQEkiEAQgZRUVFys3NlTFG0pGOZ25urlJSUpSQkGBxdAAQPm644QaVlpbqkUce0Y8//qju3btr+fLlSkxMtDo0oN65XC6lpKTUy7WqG3XpL3l5ecyKARASWCwfQEgwxmjOnDnHLK9IjgEA6seECRO0bds2lZeXa+3atbr44outDgkNjM//5sNB+KiuHQCABo8RYQBCQmFhoQoKCqqUu91uFRQUqLCwUJ06dar/wAAAQLXKy8u9X9vftVsYyckpLy9X48aNa1T3PklRfr6+kXTov183kuTPyYsHJT3px/MBQENAIgxASEhMTFSfPn20bt06ud1ub7ndbldSUhLTcQAAgOWiJEX5NVV1ROC2m2C027FUHgno9gTXz6lyvIxoRDgiEQYgJNhsNk2aNEmjR4+utpzFXQEAaFgq7xbqvsodXJ9MDv9vFBu7noanyiMaV/5QYmEkJ6c2IxqBUMEaYQBCRkJCglJTU71JL5vNptTUVLVv397iyAAAwNF8blJFBuGjunYAABq8YLrvAvhdfn6+srOzlZ6eruTkZKvDgR+kpaVp+fLlKikpUVxcnFJTU60OCQAAhLHKU8/2SYo6wXTDymt+BdqJ1hQ7WOlrptD5qjwScGC7ONkjgich6vYY7yi2moxorPy7L3cfPE7NhqdyvLyGUYFEGMKWy+VSVlaWSkpKlJWVpaSkJDmdTqvDwklyOp2aMmWKN8HJ7xQAAFip8hS6qvtbBw+m0PmqPBLQHmFTZBAlwiqryYjGyq/he1bOCmQ4AcVrGBWYGomwlZOTo9LSUklSaWmpcnNzLY4I/pKcnKw33niDUX4AAAAAAB+MCENYKioqUm5urnd4rDFGubm5SklJUUJCgsXRAQAAIFTExsZq6dKlNa5vjPEZgRNIDoejxmucxcbGBjgaNFSVp08+NfBuOexRFkZTO+Xug95RbGxsgQokwhB2jDGaM6fqwPSK8lmzZrHoKQAAAPwiIiJCLVq0sDoMoM4qfzZy2KPkiAyeRFhlfMZDBRJhCDuFhYUqKCioUu52u1VQUKDCwkJ16tSp/gMDAAAAQsRhj/+X/DfGyO05LEmyR0T6NbERiHgBNEwkwhB2EhMT1adPH61bt05ut9tbbrfblZSUpMTERAujAwAAx/XfD8F+Zcz/zhsRKflz1EAg4gWCwLL1z1kdAgBUi0QYwo7NZtOkSZM0evToassZMgsAQMPVZB2b24Qkf+cLjaSK+512Sf7u3pHfBICgRSIMYSkhIUGpqalauHChjDGy2WxKTU1V+/btrQ4NAAAg7NjftVsdAvzA6XQqLy8vYOd3uVwaPny4JGnp0qVyOp0BuU6gzgugYSARhrCVlpam5cuXq6SkRHFxcUpNTbU6JAAAUI1w/XBd7rbpyNAm/zFGOug58nVUhH9ngR6JF+HMZrMpOjq6Xq7ldDrr7VoAQkvYJsKMMXK5XDWuX7lubZ7ndDqZatdAOZ1OTZkyRdnZ2UpPT+fODwAADVS4frie+Elzq0MIqEAmOOsruSkxeggAgk3YJsJcLpdSUlLq9NyKf6o1kZeX12A6U6gqOTlZycnJVocBAAAQduorwdmQkpsITW5jJI//zmeMkee/g0EjbPL7wAq38e9IUyDYhG0iDAAAAGhownUaKBDMVn5fYnUIAGohbBNhte1kGGNUXl4uSXI4HDXOytMJAAAAQE2F6zRQAMGh3H3Qr+czxuig55AkKSqikd9Hv/k7XoSGsE2E1aWT0bhx4wBFAwAAAAAIFuG6xt09K2cFKBKg/oRtIqwu8vPzvQurs65UaHjppZeUk5OjtLQ03XLLLVaHAwAAACAIsMYdELxIhNWQy+VSVlaWSkpKlJWVpaSkJKY9Brmff/5ZOTk58ng8ysnJ0XXXXafmzZtbHRYAAAAANBjhOvoNoYtEWA3l5OSotLRUklRaWqrc3FyNGzfO4qhwMqZNmyaP58j2Lh6PRw8++KCeeeYZi6MCAAAAgIaD0W8INRFWBxAMioqKlJubK/PfbWaNMcrNzVVRUZHFkaGu1qxZo40bN/qUbdiwQWvWrLEoIgAAAAAAEGgkwk7AGKM5c+Ycs7wiOYbg4fF4lJGRUe2xjIwM7ygxAAAAAAAQWpgaeQKFhYUqKCioUu52u1VQUKDCwkJ16tSp/gNDna1evVplZWXVHisrK9Pq1avZDAF+YYyRy+UKyLkrnzdQ16jgdDr9vpU1AAAAAGtUHtCzf7/UqNGJ6kuHDwc4KEmRkdKJPnYcOvS/r+s6MIlE2AkkJiaqT58+Wrdundxut7fcbrcrKSlJiYmJFkZXM7X5MH4yH66t/rBc03aee+65iomJqTYZFhMTo3PPPVcHDhw47jmsbiuCg8vlUkpKSsCvU7HAaKDk5eWxXgMAAAAQIsrLy71fL/xT8G4iUF5ersaNG9f6eX5PhGVmZurtt9/WP//5T0VHR6t///568skndeaZZ3rrGGM0ffp0zZs3T7t379b555+vZ599Vt26dfN3OCfNZrNp0qRJGj16dLXlwZAMqeuH8dp+uLb6w7I/kg5lZWUaMmTICetZ3VYAAAAAAFB7fk+ErVq1ShMnTlSfPn10+PBhTZs2TYMHD9bXX3+tJk2aSJJmzpyp2bNna/78+erSpYsee+wxXX755dqyZYuaNWvm75BOWkJCglJTU7Vw4UIZY2Sz2ZSamqr27dtbHRqAIDGwfZzsfkycG2Pk+e9I4Aib/J6Udxujld+X+PWcAAAA4SpcZumEisqzwY7FGFNv60tHREQc9/dak3gri42N1dKlS2tc3xjjM4osUBwOR61ev7GxsXW6jt8TYe+//77P96+++qpat26ttWvX6uKLL5YxRtnZ2Zo2bZquueYaSdKCBQsUHx+vRYsWafz48f4OyS/S0tK0fPlylZSUKC4uTqmpqVaHVGNOp1N5eXk1qlv5BV7bF6HTae2Qytq0U5J27drlHekXERGh1157rcZ/SFa3FcHHbrMpMsKfnZIAd3DYMwIAAMBvwmWWTm3XyG2oSb+//e1vATlvQxEREaEWLVpYHYZlAr5G2J49eyRJLVu2lCR99913Ki4u1uDBg711HA6HBgwYoM8++6zBJsKcTqemTJmi7OxspaenB1UixGaz1erNsC5zbBuC2razdevW3q9vvPFGtWnTJhBhAQAAAEBYOJnlaoIt6YfgFdBEmDFGkydP1oUXXqju3btLkoqLiyVJ8fHxPnXj4+NVWFhY7XnKy8t9huEda8e/QEtOTmY3wRA1ZswYq0MAcBz5+fneGxG8DwMAgGATLrN0glltZxjV13RBqXavA14DJxbQRNjtt9+uDRs2VDus8OhfYsXaW9XJzMzU9OnTAxIjAKBhc7lcmjFjhvbu3asZM2borbfe4h88AAAIKuEyS+dkkklWJ/1q+zuSgvf3FO4Clgi74447tGzZMn3yySdKSEjwlldMPysuLlbbtm295bt27aoySqzC1KlTNXnyZO/3ZWVl6tChQ4AiBwA0JPPnz9fevXslSXv37tWCBQsa7DR6AACAcEYyCcEgwt8nNMbo9ttv19tvv62PPvpInTt39jneuXNntWnTRitWrPCWHTx4UKtWrVL//v2rPafD4VBMTIzPAwAQ+oqKirR48WKfskWLFqmoqMiiiAAAAAAEM78nwiZOnKicnBwtWrRIzZo1U3FxsYqLi3XgwAFJRzLE6enpmjFjht555x199dVXuummm9S4cWONGjXK3+EAAIKUMUaZmZkyxtSoHAAAAABOxO9TI+fOnStJGjhwoE/5q6++qptuukmSdO+99+rAgQOaMGGCdu/erfPPP18ffPCBmjVr5u9wAABBatu2bdq4cWO1xzZu3Kht27ZVGXUMAAAAAMfj90RYTe7Q22w2ZWRkKCMjw9+XBwAAAAAAAKrl96mRAAD4Q6dOndSzZ89qj51zzjnq1KlT/QYEAAAAIOiRCAPCRH5+vkaMGKH8/HyrQwFqxGaz6f7776/22P3331+r7bUBAAAAQCIRBoQFl8ulrKws7dy5U1lZWXK5XFaHBNTY0Qkvm83GQvkAAAAA6sTva4QB/mSMCVjSpvJ5A50Ycjqdlo5eycnJUWlpqSSptLRUubm5GjdunGXxADVhjNGcOXOq3TVyzpw5mjVrFqPCAAAAANQKiTA0aC6XSykpKQG/zvDhwwN6/ry8PEVHRwf0GsdSVFSk3NxcbzLBGKPc3FylpKQoISHBkpiAmigsLFRBQUG1xwoKClRYWMg6YQAAAABqhamRQAirGDlzrHKml6Eh69ixo2JiYqo9FhMTo44dO9ZzRAAAAACCHSPCEDTcV7n9+4o1ktz//douyd8zrA5L9nftfj5p7RxrRI3b7WZEDSxT0ynP27dvV1lZWbXHysrK9O23354wGWb1tGQAAAAADQuJMASPSPn/FdvIz+drYBITE9WnTx+tW7dObrfbW26325WUlKTExEQLo0O48teU51tvvfWEdayclgwAAACg4WFqJBDCbDabJk2adMxyRsoAAAAAAMIJI8KAEJeQkKDU1FQtXLhQxhjZbDalpqaqffv2VoeGMOV0OpWXl1fj+i+//LJef/117/ejRo3SmDFjanwtAAAAAKhAIgwNms9i7oeti6NOKsVr9aL0aWlpWr58uUpKShQXF6fU1FRL40F4s9lstZqumJqa6k2ExcXF6aabbiLBBQAAAKBOSIShQSsvL/d+bfXC8yejvLxcjRs3tuz6TqdTU6ZMUXZ2ttLT00kiIKhUfr3ecccdvH4BAAAA1BmJMCBMJCcnKzk52eowgJNywQUXWB0CAAAAgCBGIgwNmsPh8H7tvsodXK/Yw/8bxVa5HQAAAAAAwBrsGokGLaC7GhodWcfr8H+/DqCGsDtjfn6+RowYofz8fKtDAQAAAADAEsE0vgZhLpjXCLOay+VSVlaWSkpKlJWVpaSkJNZZAgAAAACEHUaEAWEgJydHpaWlkqTS0lLl5uZaHBEAAAAAAPWPEWFo0JxOp/Ly8gJybpfLpeHDh0uSli5dGtARUlaOvioqKlJubq6MOTL/0xij3NxcpaSkKCEhwbK4AAChZ9u2bXr00Uf10Ucfqbi4WO3atVNaWpqmTZumqKgoq8MDAAAgEYaGzWazKTo6OuDXcTqd9XKd+maM0Zw5c45ZPmvWrAaxfhkAIDT885//lMfj0QsvvKDTTz9dX331lW699Vb98ssvmjVrltXhAQAAkAgDQllhYaEKCgqqlLvdbhUUFKiwsFCdOnWq/8AAACHpiiuu0BVXXOH9/tRTT9WWLVs0d+5cEmEAAKBBYI0wIIQlJiaqT58+stt9Nxqw2+3q27evEhMTLYoMABAu9uzZo5YtWx7zeHl5ucrKynweAAAAgUIiDAhhNptNkyZNOmY50yIBAIH0r3/9S08//bRuu+22Y9bJzMxUbGys99GhQ4d6jBAAAIQbEmFAiEtISFBqaqo36WWz2ZSamqr27dtbHBkAIFhkZGTIZrMd97FmzRqf5/zwww+64oorNGLECN1yyy3HPPfUqVO1Z88e72PHjh2Bbg4AAAhjrBEGhIG0tDQtX75cJSUliouLU2pqqtUhAQCCyO23364bb7zxuHUqrzn5ww8/aNCgQerXr5/mzZt33Oc5HA45HA5/hIkQZoyRy+Wqcf3KdWvzPOnIJkqMmgeA0EUiDAgDTqdTU6ZMUXZ2ttLT0+V0Oq0OKSwYY7xfuz3mODUbnsrxVm4HgPAUFxenuLi4GtX9/vvvNWjQICUlJenVV19VRAQTEHDyXC6XUlJS6vTc4cOH16p+Xl5eSO4mDgA4gkQYECaSk5OVnJxsdRhhpby83Pv1yh9KLIzk5JSXl6tx48ZWhwEgCPzwww8aOHCgOnbsqFmzZumnn37yHmvTpk29xcHoIQAAcCwkwgAAAOAXH3zwgbZu3aqtW7cqISHB51h9ji5l9FDocTqdysvLq3F9Y4z3hpTD4ahVspKR8wAQ2kiEAUCAVF7zZmC7ONkjgmfEgNtjvKPYWLsHQE3ddNNNuummm6wOAyHIZrPVOuHIaGYAQHVIhCFkMA0CDU3l14g9wqbIIEqEVcZrHUCwYfQQAAA4FhJhCBlMgwAAABKjhwAAwLGxjQ8QJvLz8zVixAjl5+dbHQoAAAAAAJZgRBhCRm2nQcyfP1+vvfaajDGy2WwaOXKkxowZU+NrBROXy6WsrCyVlJQoKytLSUlJQdcGAAAAAABOFiPCEDIqpkHU5FFaWqrXX3/du4OVMUavv/66SktLa/T8YFszKScnRyUlRxY+LykpUW5ursURAQAABBaj4QEA1SERhrBjjNGcOXOOWV6f27vXh6KiIuXk5PiU5eTkqKioyKKIAAAAAqtiNPzOnTuVlZVV642RUD+MMTpw4ECNH0dvdlXT54Va/x7AyWFqJMJOYWGhCgoKqpS73W4VFBSosLBQnTp1qv/AAuBYyT2Px6M5c+Zo1qxZQTe6DQAA4ERycnJUWloqSSotLVVubq7GjRtncVQ4Wn1tdsVGVwAqY0QYwk5iYqL69OlTJQFks9nUt29fJSYmWhSZ/1Uk/Y5OhBljvEk/AACAUFJUVKTc3FyfJTByc3MZDQ8AkMSIMIShioXxjx4VZozRyJEjQ2qEVMeOHRUTE6OysrIqx2JiYtSxY0cLogIAAAiMEy2BwWj4hqW2m11NnjxZmzZt8n7fvXt3ZWVl1eg6AFCBEWEIO8YYLV68uNoRYYsWLQqpNQS2b99ebRJMksrKyrR9+/Z6jggAACBwKkbDu91un/LKS2Cg4ajNZlebNm3ySYJJ0ldffaVNmzaF3EZXAAKLEWEIO8daI6zydMFQWSOsYhpode0NtWmgsI4xJqCLEB+9MG6gOJ1OOsoAEOQq+j7r1q3zSYbZ7XYlJSXR9wlSHo9HGRkZ1R7LyMjQsmXLFBHBGA8ANUMiDGEnnDpIx5oGKinkpoHCOiez0G1t1WZh3NpiIV0ACH42m02TJk3S6NGjqy2n7xOcVq9efdxZDqtXr1ZycnI9RwUgWJE2R9ip6AgdqzyUOkgV00CrE2rTQAEAOBn5+fkaMWKE8vPzrQ4FJykhIUGpqanePp3NZlNqaqrat29vcWSoq379+ikmJqbaY7GxserXr189RwQgmDEiDGGpooO0cOFCGWNCtoN0rGmgkkJuGigahqcG3i2HPcqv5zTG6KDnkCQpKqKRX5PV5e6DumflLL+dD0BwcrlcysrKUklJibKyspSUlMTi2kEuLS1Ny5cvV0lJieLi4pSammp1SDgJERERysjI0OTJk6scmz59OtMiAdQK7xgIW2lpaWrVqpUkhWwHqWLXyOqwayQCwWGPkiPSvw9nI4diHE0V42gqZyOHf8/v56QdgOCUk5Oj0tJSSVJpaalyc3Mtjggny+l0asqUKYqPj9fkyZNJbIaA3r17q1u3bj5l3bt3V69evSyKCECwYkQYwlZFByk7O1vp6ekh2UGqya6RjAgDAISzoqIi5ebmepcLMMYoNzdXKSkpSkhIsDi6E6vthiV13YAkGDcUSU5OZt2oENOtWzefnSOPTowBQE2QCENYC/UOUseOHdW0aVPt27evyrGmTZsyIqweuY2RPP47nzFGnv8u8RZhk98/nLhZPw5AGDDGaM6cOccsnzVrVoNP/pzMhiW12YAkGDcUyc/P997wDOX+XrgoKirSW2+95VP21ltvafjw4UGRtAbQcJAIA0JYYWFhtUkwSdq3b58KCwvVuXPneo4qPK38vsTqEAAARznWWpput5u1NIMc676FllBIWgNoOEiEAQAAICwlJiaqT58+Wrdundxut7fcbrcrKSlJiYmJFkZXM06nU3l5eTWub4xReXm5JMnhcNQ4eRBsSaTq1n0bN26cxVGhrkhaA/AnEmFACOvUqZN69uypDRs2VDl2zjnn0GEIsNp+OKkNl8vlndKydOnSgH5ACbYPPwBQUzabTZMmTdLo0aOrLQ+GESY2m63WUxYbN24coGgahmBf9w1VhULSGkDDQSIMCGE2m039+vWrNhHWr1+/oOjgB7O6fDipC6fTGXTrtgBAQ5GQkKDU1FQtXLhQxhjZbDalpqaqffv2VoeGOmAKXWgKhaQ1gIYjwuoAAASO2+3Wiy++WO2xefPm+dxRAwAgXKWlpalVq1aSpLi4OKWmplocEeqqYgrd0X2cylPoEJwqktYVSS+S1gDqikQYEMKWLl0qj6f6rQo9Ho+WLl1azxEBANDwOJ1OTZkyRfHx8Zo8eTJTwoNYxRQ6u93uU26329W3b1+m0AU5ktYA/IFEGBDCzjnnnJM6DgBAuEhOTtYbb7yh5ORkq0PBSaiYKnescqbQBTeS1gD8gUQYEMJO1NmjMwgAAEINU+hCG0lrACeLxfKBEEYiDPWhYlcuSSp3H7QwktqrHG/ldgAAgltaWpqWL1+ukpISptABAHyQCANCWMeOHRUREVHtOmERERHq2LGjBVEh1JSXl3u/vmflLAsjOTnl5eVq3Lix1WEAAPygYgpddna20tPTmUIHAPAiEQaEsM8///y4i+V//vnnDCsHAAAhKTk5mX4OAKAKEmFACGvbtu1JHQdqwuFweL9+auDdctijLIymdsrdB72j2Cq3AwAAAEBoIhEGhLBOnTopKipKBw9WXbfJ4XCoU6dO9R8UQk7lteYc9ig5IoMnEVYZa+YBAAAAoY9dI4EQtm3btmqTYNKR9ZC2bdtWvwEBAAAAAGAhEmFACNuxY8dJHQcAAAAAIJQwNRIIYd98880Jjw8YMKCeokE4KHdXPwLxZBhjdNBzSJIUFdHIr1MYAxEvAAAAgIaLRBgQhIwxcrlcJ6zXt29fLVy48LjHDxw4cNxzOJ1O1k6qJzX9vUryqVfT51QI5O+0YuH5UOXxeLRnz54a1zfGqLy8PIARHeFwOGr1O42NjVVExPEHhdfm9VhRvyG2lfcwAAAAVGZpIuy5557TU089pR9//FHdunVTdna2LrroIitDAoKCy+VSSkrKSZ/njjvuOGGdvLw8RUdHn/S1cGJ1/b0OHz68VvX5ndbdnj17av3zboiWLl2qFi1aHLeOv95nrMbrHQBCS35+vrKzs5Wenq7k5GSrwwEQhCxLhC1ZskTp6el67rnnlJycrBdeeEFDhgzR119/rY4dO1oVFmCJ2o68qO0IoJNRm2sx8iI8OZ1O5eXlBez8LpfLm3xaunSpnE5nQK4TqPMCAAD/cLlcysrKUklJibKyspSUlMT/bwC1ZlkibPbs2Ro3bpxuueUWSVJ2drby8vI0d+5cZWZmWhUWYImGPPKiNqNfGHlxcmqTUKo8Da0uU8X8yWaz1dvv3el0Wvoaczgc3q/79esnu91+3PrGGHk8nkCHpYiIiBO+Btxut1avXi3Jtx01MXacS40aHb+OMdLhw7U6bZ1ERkonerkfOiS98jIfjAAg1OTk5Ki0tFSSVFpaqtzcXI0bN87iqAAEG0sSYQcPHtTatWt1//33+5QPHjxYn332mRUhAZYyxlgdgl+ESjusUtuEUuPGjQMYTeCczAhIq9dDq3wuu91eo0RYfYySrEkirLKa1K3893zo0InPWV+JMGNqlgj7X33elwAgFBQVFSk3N9f7vm6MUW5urlJSUpSQkGBxdACCiSWJsJKSErndbsXHx/uUx8fHq7i4uEr98vJynwV4y8rKAh4jUJ/qY4Hp+lBeXh60yRnUn5MZAdmQ1kP729/+FpDzNhSV35cW/il4R1fxvgQAwc8Yozlz5hyzfNasWSzPAaDGjr9lVIAd/WZ1rDvnmZmZio2N9T46dOhQXyECAAAAACxUWFiogoICud1un3K3262CggIVFhZaFBmAYGTJiLC4uDjZ7fYqo7927dpVZZSYJE2dOlWTJ0/2fl9WVkYyDCElNjZWS5curXH9yutDBVpt1p+KjY0NcDQIBbVdXL8hrYd2MrEHUiB+Lg31fam2beV9CQCCX2Jiovr06aN169b5JMPsdruSkpKUmJhoYXQAgo0libCoqCglJSVpxYoV+vWvf+0tX7FiRbXTXhwOR60X9gWCSUREhFq0aGF1GEC9qMvi+g1lalswx15bvC8BABoKm82mSZMmafTo0dWWMy0SQG1YNjVy8uTJeumll/TKK69o8+bNmjRpkrZv367bbrvNqpAAAAAAAA1QQkKCUlNTvUkvm82m1NRUtW/f3uLIAAQbS0aESdINN9yg0tJSPfLII/rxxx/VvXt3LV++nGGtAAAAAIAq0tLStHz5cpWUlCguLk6pqalWhwQgCFm6WP6ECRO0bds2lZeXa+3atbr44outDAcAAAAA0EA5nU5NmTJF8fHxmjx5st/XAgUQHiwbEQYAAAAAQG0kJycrOTnZ6jAABDFLR4QBAAAAAAAA9YVEGAAAAAAAAMICiTAAAAAAAACEBRJhAAAAAAAACAskwgAAAAAAABAWSIQBAAAAAAAgLJAIAwAAAAAAQFggEQYAAAAAAICwQCIMAAAAAAAAYSHS6gDqwhgjSSorK7M4EgAAEEwq+g4VfQk0PPTzAABAXdS0nxeUibC9e/dKkjp06GBxJAAAIBjt3btXsbGxVoeBatDPAwAAJ+NE/TybCcJboh6PRz/88IOaNWsmm81Wb9ctKytThw4dtGPHDsXExNTbdetbuLRToq2hKlzaGi7tlGhrKLKqncYY7d27V+3atVNEBCtENET08wIvXNoaLu2UaGsoCpd2SrQ1FDX0fl5QjgiLiIhQQkKCZdePiYkJ6RdthXBpp0RbQ1W4tDVc2inR1lBkRTsZCdaw0c+rP+HS1nBpp0RbQ1G4tFOiraGoofbzuBUKAAAAAACAsEAiDAAAAAAAAGGBRFgtOBwOPfzww3I4HFaHElDh0k6JtoaqcGlruLRToq2hKFzaieARTq/JcGlruLRToq2hKFzaKdHWUNTQ2xmUi+UDAAAAAAAAtcWIMAAAAAAAAIQFEmEAAAAAAAAICyTCAAAAAAAAEBZIhAFh6qabbtLVV19tdRhASLLZbPrzn/9sdRhBZeXKlbLZbPr555+tDgUAAAAhzPJEmM1mO+7jpptusjpEvxs4cKDS09MtjeGmm27y/owjIyPVsWNH/e53v9Pu3bu9dTp16qTs7Owqz83IyNC5555bf8HW0fPPP69mzZrp8OHD3rJ9+/apUaNGuuiii3zqfvrpp7LZbPrmm2/qO8w6qcnv70T+8Ic/aP78+YELso4qt63yY+vWrcc9Vvm5t912W5XzTpgwodr3lOLiYt1xxx069dRT5XA41KFDB1111VX68MMP66O5knzb3KhRI8XHx+vyyy/XK6+8Io/H463XqVMn2Ww2vfbaa1XO0a1bN9lstiq/0y+++EIjRoxQfHy8nE6nunTpoltvvbXBvtYrJ2h37dql8ePHq2PHjnI4HGrTpo1SUlK0evVqb/1jvU8FWkN43dQnf7znnEj//v31448/KjY21m/nBGrqueeeU+fOneV0OpWUlKRPP/3U6pAC4pNPPtFVV12ldu3ahXTCPjMzU3369FGzZs3UunVrXX311dqyZYvVYQXE3Llz1bNnT8XExCgmJkb9+vXTe++9Z3VYAZeZmSmbzWb5Z6pAyMjIqNLXbdOmjdVhBcz333+vtLQ0tWrVSo0bN9a5556rtWvXWh2WX1X04Y9+TJw40erQ/O7w4cN68MEH1blzZ0VHR+vUU0/VI4884vOZpiGwPBH2448/eh/Z2dmKiYnxKfvDH/5gdYg1dujQoaC63hVXXKEff/xR27Zt00svvaR3331XEyZM8FN01hs0aJD27dunNWvWeMs+/fRTtWnTRgUFBdq/f7+3fOXKlWrXrp26dOliRah1crK/v9jYWDVv3jxwAZ6EirZVfnTu3PmExySpQ4cOeu2113TgwAFvmcvl0uLFi9WxY0ef62zbtk1JSUn66KOPNHPmTG3cuFHvv/++Bg0aVO//mCr/Pt977z0NGjRId911l4YNG+aTzO3QoYNeffVVn+d+/vnnKi4uVpMmTXzK//KXv+iCCy5QeXm5cnNztXnzZi1cuFCxsbH6/e9/Xy/tOhnXXnutvvzySy1YsEDffPONli1bpoEDB+o///mPpXE1pNdNfQr0/4yoqCi1adNGNpvNb+cEamLJkiVKT0/XtGnT9MUXX+iiiy7SkCFDtH37dqtD87tffvlF55xzjp555hmrQwmoVatWaeLEifr888+1YsUKHT58WIMHD9Yvv/xidWh+l5CQoCeeeEJr1qzRmjVrdMkll2j48OHatGmT1aEFTEFBgebNm6eePXtaHUrAdOvWzaevu3HjRqtDCojdu3crOTlZjRo10nvvvaevv/5aWVlZDfYzSl0VFBT4/D5XrFghSRoxYoTFkfnfk08+qeeff17PPPOMNm/erJkzZ+qpp57S008/bXVovkwD8uqrr5rY2FifsmXLlplevXoZh8NhOnfubDIyMsyhQ4e8xyWZ559/3gwdOtRER0ebs846y3z22Wfm22+/NQMGDDCNGzc2F1xwgdm6dav3OQ8//LA555xzzPPPP28SEhJMdHS0ue6668zu3bt9rv3KK6+Ys846yzgcDnPmmWeaZ5991nvsu+++M5LMkiVLzIABA4zD4TCvvPKKKSkpMTfeeKNp3769iY6ONt27dzeLFi3yPm/MmDFGks/ju+++q7bt77zzjqn8K6qI++WXXzadO3c2NpvNeDwe8/PPP5tbb73VnHLKKaZZs2Zm0KBBZv369cf9WY8ZM8YMHz7cp2zy5MmmZcuW3u8TExPNnDlzqjy3Io5g0K5dO5OZmen9/t577zUTJ040Xbt2NStWrPCWX3LJJSY1NdUYc6R9HTp0MFFRUaZt27bmjjvuqPe4T+REv7/Dhw+bsWPHmk6dOhmn02m6dOlisrOzj3uOAQMGmDvuuMPcc889pkWLFiY+Pt48/PDDAW5JVdW1rSbHKh/v0aOHycnJ8Zbn5uaaHj16mOHDh5sxY8Z4y4cMGWLat29v9u3bV+VcR78fBNKx2vXhhx8aSebFF180xhz5m7z//vuNw+Ew27dv99a79dZbzR133GFiY2PNq6++aowx5pdffjFxcXHm6quvrvaa9dm+2qj4WezevdtIMitXrjxu/WO9TwVSTV43ksw777zjLb/33nvNGWecYaKjo03nzp3Ngw8+aA4ePOg9vn79ejNw4EDTtGlT06xZM9OrVy9TUFBgjDFm27ZtZtiwYaZ58+amcePGpmvXruavf/2r97mbNm0yQ4YMMU2aNDGtW7c2aWlp5qeffvIef+ONN0z37t2N0+k0LVu2NJdeemm1sR9PTf5nHO9/pjHG5Ofnm3POOcc4HA6TlJTk/R/3xRdfGGOM+fjjj40kn9fmm2++abp27WqioqJMYmKimTVrls85ExMTzeOPP25uvvlm07RpU9OhQwfzwgsv1KptQN++fc1tt93mU3bWWWeZ+++/36KI6sfR71OhbNeuXUaSWbVqldWh1IsWLVqYl156yeowAmLv3r3mjDPOMCtWrDADBgwwd911l9Uh+V0wfdY6Wffdd5+58MILrQ6j3t11113mtNNOMx6Px+pQ/G7o0KFm7NixPmXXXHONSUtLsyii6lk+Iux48vLylJaWpjvvvFNff/21XnjhBc2fP1+PP/64T71HH31Uv/nNb7R+/XqdddZZGjVqlMaPH6+pU6d6RwPdfvvtPs/ZunWrXn/9db377rt6//33tX79ep87+S+++KKmTZumxx9/XJs3b9aMGTP0+9//XgsWLPA5z3333ac777xTmzdvVkpKilwul5KSkvSXv/xFX331lX77299q9OjR+vvf/y7pyHS0fv366dZbb/VmhDt06FDjn0lF3G+99ZbWr18vSRo6dKiKi4u1fPlyrV27Vr169dKll15aq1ET//73v/X++++rUaNGNX5OMBg4cKA+/vhj7/cff/yxBg4cqAEDBnjLDx48qNWrV2vQoEF68803NWfOHL3wwgv69ttv9ec//1k9evSwKvwaO/r35/F4lJCQoNdff11ff/21HnroIT3wwAN6/fXXj3ueBQsWqEmTJvr73/+umTNn6pFHHvHesQgmN998s8+oqVdeeUVjx471qfOf//xH77//viZOnFhlJJWkBnEn6pJLLtE555yjt99+21sWHx+vlJQU73vR/v37tWTJkirty8vLU0lJie69995qz90Q2nc8TZs2VdOmTfXnP/9Z5eXlVofjVdfXTbNmzTR//nx9/fXX+sMf/qAXX3xRc+bM8R5PTU1VQkKCCgoKtHbtWt1///3ev+eJEyeqvLxcn3zyiTZu3Kgnn3xSTZs2lXRkVPWAAQN07rnnas2aNXr//fe1c+dOXX/99d7jI0eO1NixY7V582atXLlS11xzjYwxJ/VzOPo950T/M/fu3aurrrpKPXr00Lp16/Too4/qvvvuO+411q5dq+uvv1433nijNm7cqIyMDP3+97+vMv03KytLvXv31hdffKEJEybod7/7nf75z3+eVPsQPg4ePKi1a9dq8ODBPuWDBw/WZ599ZlFU8Lc9e/ZIklq2bGlxJIHldrv12muv6ZdfflG/fv2sDicgJk6cqKFDh+qyyy6zOpSA+vbbb9WuXTt17txZN954o/79739bHVJALFu2TL1799aIESPUunVrnXfeeXrxxRetDiugDh48qJycHI0dOzYkR8FfeOGF+vDDD73LsHz55Zf629/+piuvvNLiyI5idSausqNHRV100UVmxowZPnUWLlxo2rZt6/1eknnwwQe9369evdpIMi+//LK3bPHixcbpdHq/f/jhh43dbjc7duzwlr333nsmIiLC/Pjjj8YYYzp06OAzkssYYx599FHTr18/Y8z/RoQdPcqmOldeeaWZMmWK9/vq7l7UdERYo0aNzK5du7xlH374oYmJiTEul8vnuaeddtpx74qPGTPG2O1206RJE+N0Or2j02bPnu2tk5iYaKKiokyTJk18Ho0aNQqauxTz5s0zTZo0MYcOHTJlZWUmMjLS7Ny507z22mumf//+xhhjVq1aZSSZf/3rXyYrK8t06dLFZ6RGQ1ST39/RJkyYYK699lqfcxw9IuzoOzJ9+vQx9913n9/jP57Kbat4XHfddSc8VnF8+PDh5qeffjIOh8N89913Ztu2bcbpdJqffvrJZ0TY3//+dyPJvP322/Xavuocb6TbDTfcYM4++2xjzP9GP/35z3/23kVasGCBOe+884wxxmdE2JNPPmkkmf/85z/10QS/qfyzePPNN02LFi2M0+k0/fv3N1OnTjVffvmlT/36HhFW09eNTjDSYubMmSYpKcn7fbNmzcz8+fOrrdujRw+TkZFR7bHf//73ZvDgwT5lO3bsMJLMli1bzNq1a40ks23btuPGeyInes850f/MuXPnmlatWpkDBw54j7/44ovHHRE2atQoc/nll/uc85577jFdu3b1fp+YmOhzh9Hj8ZjWrVubuXPnnlR7ET6+//57I8nk5+f7lD/++OOmS5cuFkVVP070PhUqPB6Pueqqq0J61MmGDRtMkyZNjN1uN7GxsT6jhkPJ4sWLTffu3b3/S0J1RNjy5cvNm2++aTZs2OAd+RYfH29KSkqsDs3vHA6HcTgcZurUqWbdunXm+eefN06n0yxYsMDq0AJmyZIlxm63m++//97qUALC4/GY+++/39hsNhMZGWlsNluVnE5DEFmvWbdaWrt2rQoKCnxGgLndbrlcLu3fv1+NGzeWJJ/54fHx8ZLkM4onPj5eLpdLZWVliomJkSR17NhRCQkJ3jr9+vWTx+PRli1bZLfbtWPHDo0bN0633nqrt87hw4erLOLbu3dvn+/dbreeeOIJLVmyRN9//73Ky8tVXl5e7ciBukhMTNQpp5zi/X7t2rXat2+fWrVq5VPvwIED+te//nXccw0aNEhz587V/v379dJLL+mbb77RHXfc4VPnnnvuqbK4+B//+Ed98sknJ9eQejJo0CD98ssvKigo0O7du9WlSxe1bt1aAwYM0OjRo/XLL79o5cqV6tixo0499VSNGDFC2dnZOvXUU3XFFVfoyiuv1FVXXaXIyIb3p3Ki39/zzz+vl156SYWFhTpw4IAOHjx4wk0Ojl5roW3bttq1a1cgwj+uirZVqPz3c7xjFeLi4jR06FAtWLBAxhgNHTpUcXFxPnXMf0fENPQ7McaYKjEOHTpU48eP1yeffFLtaLeK5wW7a6+9VkOHDtWnn36q1atX6/3339fMmTP10ksvWbaRSl1fN2+++aays7O1detW7du3T4cPH/b+P5KkyZMn65ZbbtHChQt12WWXacSIETrttNMkSXfeead+97vf6YMPPtBll12ma6+91vu3unbtWn388cfeEWKV/etf/9LgwYN16aWXqkePHkpJSdHgwYN13XXXqUWLFrVu+7Hec3766acT/s/csmWLevbsKafT6T3et2/f415v8+bNGj58uE9ZcnKysrOz5Xa7ZbfbJfm+b1UsKGzF+xaC29F/09W99yI43X777dqwYYP+9re/WR1KwJx55plav369fv75Z7311lsaM2aMVq1apa5du1odmt/s2LFDd911lz744AOf/yWhaMiQId6ve/TooX79+um0007TggULNHnyZAsj8z+Px6PevXtrxowZkqTzzjtPmzZt0ty5c/Wb3/zG4ugC4+WXX9aQIUPUrl07q0MJiCVLlignJ0eLFi1St27dtH79eqWnp6tdu3YaM2aM1eF5NeipkR6PR9OnT9f69eu9j40bN+rbb7/1eQOsPJ2votNSXdnxdiqoqGOz2bz1XnzxRZ9rf/XVV/r88899nnf0h/CsrCzNmTNH9957rz766COtX79eKSkpOnjw4HHbGhERUeWDa3WL4R99PY/Ho7Zt2/rEuX79em3ZskX33HPPca/ZpEkTnX766erZs6f++Mc/qry8XNOnT/epExcXp9NPP93nEUzDyk8//XQlJCTo448/1scff6wBAwZIktq0aaPOnTsrPz9fH3/8sS655BJJRxYi37Jli5599llFR0drwoQJuvjii+t9I4SaON7v7/XXX9ekSZM0duxYffDBB1q/fr1uvvnmE74Oj54aW/nvoT5VtK3i0bZt2xodq2zs2LGaP3++FixYUG2i6IwzzpDNZtPmzZsD1g5/2Lx5s89mAJIUGRmp0aNH6+GHH9bf//53paamVnlexcYPwT5FzOl06vLLL9dDDz2kzz77TDfddJMefvhhy+Kpy+vm888/14033qghQ4boL3/5i7744gtNmzbN5+8xIyNDmzZt0tChQ/XRRx+pa9eueueddyRJt9xyi/79739r9OjR2rhxo3r37u1dcNTj8eiqq66q8j/g22+/1cUXXyy73a4VK1bovffeU9euXfX000/rzDPP1HfffVfrth/rPacm/zOrSyqcKFlb0+c0lPctBKe4uDjZ7XYVFxf7lO/atct7cxXB64477tCyZcv08ccf+9wADzVRUVE6/fTT1bt3b2VmZuqcc84Jqg3HamLt2rXatWuXkpKSFBkZqcjISK1atUp//OMfFRkZKbfbbXWIAdOkSRP16NFD3377rdWh+F3btm2rJGzPPvvskNysRJIKCwv1f//3f7rlllusDiVg7rnnHt1///268cYb1aNHD40ePVqTJk1SZmam1aH5aNCJsF69emnLli1VEjGnn366IiJOLvTt27frhx9+8H6/evVqRUREqEuXLoqPj1f79u3173//u8p1j/5AerRPP/1Uw4cPV1pams455xydeuqpVd60oqKiqrxZn3LKKdq7d6/PbjYVa4AdT69evVRcXKzIyMgqsR49AuZEHn74Yc2aNcvn5xIKBg0apJUrV2rlypUaOHCgt3zAgAHKy8vT559/rkGDBnnLo6Oj9atf/Up//OMftXLlSq1evToodmqp/Pv79NNP1b9/f02YMEHnnXeeTj/99BOOEAw1V1xxhQ4ePKiDBw8qJSWlyvGWLVsqJSVFzz77bLW7SP3888/1EOXxffTRR9q4caOuvfbaKsfGjh2rVatWafjw4dWO7hk8eLDi4uI0c+bMas/dENpXF127drV016+6vG7y8/OVmJioadOmqXfv3jrjjDNUWFhYpV6XLl00adIkffDBB7rmmmt81rnr0KGDbrvtNr399tuaMmWKd/2MXr16adOmTerUqVOV/wEVN05sNpuSk5M1ffp0ffHFF4qKivIm2U5GxXuO2+0+4f/Ms846Sxs2bPBZ763yjr7V6dq1a5URHJ999pm6dOniHQ0GnKyoqCglJSVVWQ9zxYoV6t+/v0VR4WQZY3T77bfr7bff1kcffXTC/nuoMcY0qPU1/eHSSy/Vxo0bfW649O7dW6mpqVq/fn1I/18oLy/X5s2bj3nzN5glJydry5YtPmXffPONEhMTLYoosF599VW1bt1aQ4cOtTqUgNm/f3+VXI3dbm9wNykb3nyvSh566CENGzZMHTp00IgRIxQREaENGzZo48aNeuyxx07q3E6nU2PGjNGsWbNUVlamO++8U9dff73atGkj6cjd+TvvvFMxMTEaMmSIysvLtWbNGu3evfu4Q1JPP/10vfXWW/rss8/UokULzZ49W8XFxTr77LO9dTp16qS///3v2rZtm5o2baqWLVvq/PPPV+PGjfXAAw/ojjvu0D/+8Y8qCwJX57LLLlO/fv109dVX68knn9SZZ56pH374QcuXL9fVV19dZerm8QwcOFDdunXTjBkzQmpb7UGDBmnixIk6dOiQd0SYdCQR9rvf/U4ul8ubCJs/f77cbrf397Fw4UJFR0cHxZtx5d/fGWecoT/96U/Ky8tT586dtXDhQhUUFIRVR9But3tH7Ryrc/Tcc8+pf//+6tu3rx555BH17NlThw8f1ooVKzR37tx6HS1WXl6u4uJiud1u7dy5U++//74yMzM1bNiwaoeGn3322SopKfFOET9akyZN9NJLL2nEiBH61a9+pTvvvFOnn366SkpK9Prrr2v79u167bXXAt2sOistLdWIESM0duxY9ezZU82aNdOaNWs0c+bMKtPl6lttXzenn3669+fdp08f/fWvf/VJRB04cED33HOPrrvuOnXu3FlFRUUqKCjwJkDT09M1ZMgQdenSRbt379ZHH33k/Z8yceJEvfjiixo5cqTuuecexcXFaevWrXrttdf04osvas2aNfrwww81ePBgtW7dWn//+9/1008/+fxPqqvK7zkn+p85atQoTZs2Tb/97W91//33a/v27Zo1a5akY08znTJlivr06aNHH31UN9xwg1avXq1nnnlGzz333EnHDlQ2efJkjR49Wr1791a/fv00b948bd++XbfddpvVofndvn37tHXrVu/33333ndavX6+WLVuqY8eOFkbmXxMnTtSiRYu0dOlSNWvWzDviLzY2VtHR0RZH518PPPCAhgwZog4dOmjv3r167bXXtHLlSr3//vtWh+ZXzZo1U/fu3X3KmjRpolatWlUpD3Z33323rrrqKnXs2FG7du3SY489prKysgY1rcxfJk2apP79+2vGjBm6/vrr9Y9//EPz5s3TvHnzrA7N7zwej1599VWNGTOmQS674y9XXXWVHn/8cXXs2FHdunXTF198odmzZ1c7Q8dSlqxMdgzVLRj//vvvm/79+5vo6GgTExNj+vbta+bNm+c9rqMW+qxYxL5i8V1jqi7AW7El7XPPPWfatWtnnE6nueaaa6osKp2bm2vOPfdcExUVZVq0aGEuvvhi7wLJ1V3HGGNKS0vN8OHDTdOmTU3r1q3Ngw8+aH7zm9/4LIS9ZcsWc8EFF5jo6GgjyXz33XfGmCOL459++v+3d+8grWRxHMfnLubhAxOQKZKQFIloELlCLLRXsBHBgEYQ8VEIYkQbMaCojZWFhdhYWAixVbBSBLGwsrJQRBtJIWlNIabQ3xZLwo1vd9d4b+b7gTQzB3JOzgyH/Jn5nVo5nU51dnZqfX39WVj+SyH1mUxGExMT8nq9stls8vv96u/vVyqVevW3fi2cO5lMym63K5VKvRpC/adt6Zubq3A4XHA8FygdCoXyx7a3t9XS0qLq6mpVVlaqtbVVBwcHxe7yu96bv+vraw0NDcnlcsntdmtsbEyJRKJg3l4Ky38aOPpruHyxvBUc/9a5j5x/aTw3NzcaHx/Pbw7h8/nU1dWlw8PDT/f93xocHMyHj5eVlck0TbW3t2tjY0MPDw/5du8Fw/8alp9zcnKiaDQq0zTlcDhUW1ur0dFRXV1dfdFo/pvcHN7f3yuRSCgSicjlcqmiokL19fWam5vT3d1dvn2xw/Jz3rtunq5N09PTqqmpUVVVlWKxmFZWVvLrXTabVV9fn/x+v+x2u7xer+LxeD4MOB6PKxQKyeFwyDRNDQwMFATmXl5eqru7W263W+Xl5QqHw5qamtLj46POz8/V0dGRn/+6ujqtrq5+erwfWTPeWjMl6fj4WD9//pTdbldzc7O2trZkGIYuLi4kPV+rpX82TGhoaJDNZlMgENDy8nLB9780/01NTVpYWPj0GGFta2tr+fs5Eono6Ojou7v0JXL32dNPsdf6r/bSGA3DeLZGloKRkZH8tWuaptra2rS/v//d3SqKUg3Lj8Vi8ng8stls8nq9ikajOjs7++5ufZnd3V01NjbK4XAoHA4X/NcvJXt7e/nNjEpZJpPR5OSkAoGAnE6ngsGgZmdnlc1mv7trBX5IJZCo/EmLi4vGzs7Oh149BAAA/79kMmkMDw8bt7e3JfeEBgAAAH5fpftMHgAA+G1sbm4awWDQ8Pl8xunpqTEzM2P09vZSBAMAAEBRUQgDAABfLp1OG/Pz80Y6nTY8Ho/R09NjLC0tfXe3AAAAYDGWfDUSAAAAAAAA1vPX+00AAAAAAACAPx+FMAAAAAAAAFgChTAAAAAAAABYAoUwAAAAAAAAWAKFMAAAAAAAAFgChTAAAAAAAABYAoUwAAAAAAAAWAKFMAAAAAAAAFgChTAAAAAAAABYwt/nlaqr2J9W/QAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1500x500 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplots(figsize=(15, 5))\n",
    "plt.subplot(1, 2, 1)\n",
    "sns.boxplot(data=X_train)\n",
    "plt.title('X_train Before Scaling')\n",
    "plt.subplot(1, 2, 2)\n",
    "sns.boxplot(data=X_train_scaled)\n",
    "plt.title('X_train After Scaling')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Linear Regression Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 0.5468236465249985\n",
      "R2 Score 0.9847657384266951\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7f30befd5780>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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f+6557RmzRqtXbtWO3fulNvtVnV1dWSvomwx0n2SpNra2qhnbNOmTRa20B7a2tq0dOlSbd++XS0tLTp37pxqamrU3d0duYZnKrb7JPFMSdKUKVP0zDPPaNeuXdq1a5fmzp2refPmRQKG7Z4nkwVmzpxpHnrooahjf/VXf2V+/OMfp6hF9rRy5Uozffr0VDfD9iSZDRs2RN739fUZt9ttnnnmmcixnp4e43K5zC9/+csUtNAeLrxPxhizaNEiM2/evJS0x846OjqMJNPW1maM4ZkayoX3yRieqeFccskl5sUXX7Tl85TxPR9nz57V7t27VVNTE3W8pqZGW7duTVGr7OvQoUMqKSlReXm57r77bn322WepbpLteb1e+f3+qGfM6XTqjjvu4BkbRGtrq4qKinT11VfrgQceUEdHR6qblHKBQECSVFhYKIlnaigX3qcwnqlovb29Wr9+vbq7u1VVVWXL5ynjw8fx48fV29ur4uLiqOPFxcXy+/0papU9zZo1Sy+//LLeffddvfDCC/L7/Zo9e7Y6OztT3TRbCz9HPGMjq6ur029/+1u9//77+pd/+Rft3LlTc+fOVSgUSnXTUsYYo+XLl+vWW29VZWWlJJ6pwQx2nySeqfPt379fF198sZxOpx566CFt2LBBFRUVtnyebLer7VhxOBxR740xA45lu7q6usg/X3/99aqqqtLUqVP1m9/8RsuXL09hy9IDz9jI7rrrrsg/V1ZW6qabblJZWZnefvttLViwIIUtS51HHnlEH330kT788MMB53imvjbUfeKZ+to111yjffv26dSpU3rttde0aNEitbW1Rc7b6XnK+J6PyZMnKzc3d0C66+joGJACEW3SpEm6/vrrdejQoVQ3xdbCK4J4xuLn8XhUVlaWtc/Yo48+qrfeeksffPCBpkyZEjnOMxVtqPs0mGx+psaPH6+rrrpKN910kxobGzV9+nT9/Oc/t+XzlPHhY/z48brxxhvV0tISdbylpUWzZ89OUavSQygU0scffyyPx5PqpthaeXm53G531DN29uxZtbW18YyNoLOzU8eOHcu6Z8wYo0ceeUSvv/663n//fZWXl0ed55nqN9J9Gky2PlODMcYoFArZ83lKyTRXi61fv96MGzfO/PrXvzbt7e1m2bJlZtKkSebIkSOpbpqt/OhHPzKtra3ms88+M9u3bzff//73TX5+PvfJGNPV1WX27t1r9u7daySZNWvWmL1795rPP//cGGPMM888Y1wul3n99dfN/v37zT333GM8Ho8JBoMpbrm1hrtPXV1d5kc/+pHZunWr8Xq95oMPPjBVVVXm8ssvz7r7tGTJEuNyuUxra6vx+XyR15dffhm5hmdq5PvEM/W1FStWmM2bNxuv12s++ugj8+STT5qcnBzz3nvvGWPs9zxlRfgwxphf/OIXpqyszIwfP97MmDEjaqkW+t11113G4/GYcePGmZKSErNgwQJz8ODBVDfLFj744AMjacBr0aJFxpj+pZErV640brfbOJ1Oc/vtt5v9+/enttEpMNx9+vLLL01NTY257LLLzLhx48wVV1xhFi1aZI4ePZrqZltusHskybz00kuRa3imRr5PPFNfu//++yO/cZdddpn5zne+EwkextjveXIYY4x1/SwAACDbZfycDwAAYC+EDwAAYCnCBwAAsBThAwAAWIrwAQAALEX4AAAAliJ8AAAASxE+AACApQgfAADAUoQPAABgKcIHAACwFOEDAABY6v8DMOa/5mSG6j8AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.metrics import r2_score\n",
    "linreg=LinearRegression()\n",
    "linreg.fit(X_train_scaled,y_train)\n",
    "y_pred=linreg.predict(X_test_scaled)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)\n",
    "plt.scatter(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Lasso Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 1.133175994914409\n",
      "R2 Score 0.9492020263112388\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7f30bd0eb790>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh8AAAGdCAYAAACyzRGfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAqFklEQVR4nO3de3CT953v8c9jB2QgshJDbMnFcXUotHGc0kBCMM2F0OKxd+tCac/kMnSg23ISApmhpJMszekab3fiNDNh0xkaurfDtkNScs5sLrDJkrhLMGGBhXApF+fkkMQp3kauCwbJcbBI7N/5g0hBtmxJtvTo9n7NaAY9+ln65Zln5vnkd/k+ljHGCAAAwCYF6e4AAADIL4QPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2InwAAABbET4AAICtrkh3BwYbGBjQBx98IKfTKcuy0t0dAAAQB2OMenp6VF5eroKCkcc2Mi58fPDBB6qoqEh3NwAAwCh0dHRo6tSpI7bJuPDhdDolXep8cXFxmnsDAADiEQgEVFFREb6PjyTjwkdoqqW4uJjwAQBAlolnyQQLTgEAgK0IHwAAwFaEDwAAYCvCBwAAsBXhAwAA2IrwAQAAbEX4AAAAtiJ8AAAAW2VckTEAAJAa/QNGB9q71dXTp1JnkeZ4S1RYYP9z1AgfAADkgR0nfGra3iafvy98zOMqUmNDleqqPbb2hWkXAABy3I4TPq3ccjgieEhSp79PK7cc1o4TPlv7Q/gAACCH9Q8YNW1vk4nyWehY0/Y29Q9Ea5EahA8AAHLYgfbuISMelzOSfP4+HWjvtq1PhA8AAHJYV8/wwWM07ZKB8AEAQA4rdRYltV0yED4AAMhhc7wl8riKNNyGWkuXdr3M8ZbY1ifCBwAAOaywwFJjQ5UkDQkgofeNDVW21vsgfAAAkOPqqj3atHSW3K7IqRW3q0ibls6yvc4HRcYAAMgDddUeLaxyU+EUAADYp7DAUs20yenuRmLTLs3Nzbr55pvldDpVWlqqxYsX6+23345os3z5clmWFfGaO3duUjsNAACyV0Lho7W1VatWrdL+/fvV0tKiTz75RLW1tert7Y1oV1dXJ5/PF3698sorSe00AADIXglNu+zYsSPi/ebNm1VaWqpDhw7p9ttvDx93OBxyu93J6SEAAMgpY9rt4vf7JUklJZF7g3ft2qXS0lLNmDFDK1asUFdX11h+BgAA5BDLGDOqJ8kYY7Ro0SKdO3dOb7zxRvj4c889pyuvvFKVlZVqb2/XT37yE33yySc6dOiQHA7HkO8JBoMKBoPh94FAQBUVFfL7/SouLh5N1wAAgM0CgYBcLldc9+9R73ZZvXq1jh07pj179kQcv+uuu8L/rq6u1k033aTKykq9/PLLWrJkyZDvaW5uVlNT02i7AQAAssyopl0efPBBbdu2Ta+//rqmTp06YluPx6PKykqdOnUq6ufr1q2T3+8Pvzo6OkbTJQAAkCUSGvkwxujBBx/UCy+8oF27dsnr9cb8m7Nnz6qjo0MeT/TqaQ6HI+p0DAAAyE0JjXysWrVKW7Zs0bPPPiun06nOzk51dnbqwoULkqQPP/xQP/rRj7Rv3z69//772rVrlxoaGjRlyhR961vfSsl/AAAAyC4JLTi1rOglWDdv3qzly5frwoULWrx4sY4cOaLz58/L4/Hozjvv1E9/+lNVVFTE9RuJLFgBAACZIWULTmPllAkTJujVV19N5CsBAECe4am2AADAVoQPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2InwAAABbET4AAICtCB8AAMBWhA8AAGArwgcAALAV4QMAANiK8AEAAGxF+AAAALYifAAAAFsRPgAAgK0IHwAAwFaEDwAAYCvCBwAAsBXhAwAA2IrwAQAAbEX4AAAAtiJ8AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2InwAAABbET4AAICtCB8AAMBWhA8AAGArwgcAALAV4QMAANiK8AEAAGxF+AAAALYifAAAAFsRPgAAgK0IHwAAwFaEDwAAYCvCBwAAsBXhAwAA2IrwAQAAbEX4AAAAtiJ8AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwFeEDAADYivABAABslVD4aG5u1s033yyn06nS0lItXrxYb7/9dkQbY4zWr1+v8vJyTZgwQfPnz9fJkyeT2mkAAJC9Egofra2tWrVqlfbv36+WlhZ98sknqq2tVW9vb7jNE088oQ0bNmjjxo06ePCg3G63Fi5cqJ6enqR3HgAAZB/LGGNG+8d/+tOfVFpaqtbWVt1+++0yxqi8vFxr1qzRI488IkkKBoMqKyvTz372M913330xvzMQCMjlcsnv96u4uHi0XQMAADZK5P49pjUffr9fklRSUiJJam9vV2dnp2pra8NtHA6H7rjjDu3duzfqdwSDQQUCgYgXAADIXaMOH8YYrV27Vrfeequqq6slSZ2dnZKksrKyiLZlZWXhzwZrbm6Wy+UKvyoqKkbbJQAAkAVGHT5Wr16tY8eO6Te/+c2QzyzLinhvjBlyLGTdunXy+/3hV0dHx2i7BAAAssAVo/mjBx98UNu2bdPu3bs1derU8HG32y3p0giIx+MJH+/q6hoyGhLicDjkcDhG0w0AAJCFEhr5MMZo9erVev7557Vz5055vd6Iz71er9xut1paWsLHLl68qNbWVs2bNy85PQYAAFktoZGPVatW6dlnn9VLL70kp9MZXsfhcrk0YcIEWZalNWvW6LHHHtP06dM1ffp0PfbYY5o4caLuvffelPwHAACA7JJQ+Ni0aZMkaf78+RHHN2/erOXLl0uSHn74YV24cEEPPPCAzp07p1tuuUWvvfaanE5nUjoMAPhM/4DRgfZudfX0qdRZpDneEhUWRF9jB2SKMdX5SAXqfABAfHac8Klpe5t8/r7wMY+rSI0NVaqr9ozwl0Dy2VbnAwCQHjtO+LRyy+GI4CFJnf4+rdxyWDtO+NLUMyA2wgcAZJn+AaOm7W2KNmwdOta0vU39Axk1sA2EET4AIMscaO8eMuJxOSPJ5+/TgfZu+zoFJIDwAQBZpqtn+OAxmnaA3QgfAJBlSp1FSW0H2I3wAQBZZo63RB5XkYbbUGvp0q6XOd4SO7sFxI3wAQBZprDAUmNDlSQNCSCh940NVdT7QMYifABAFqqr9mjT0llyuyKnVtyuIm1aOos6H8hoo3qwHAAg/eqqPVpY5abCKbIO4QMAslhhgaWaaZPT3Q0gIUy7AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2InwAAABbET4AAICtCB8AAMBWhA8AAGArwgcAALAV4QMAANjqinR3AAAwev0DRgfau9XV06dSZ5HmeEtUWGClu1vAiAgfAJCldpzwqWl7m3z+vvAxj6tIjQ1Vqqv2pLFnwMiYdgGALLTjhE8rtxyOCB6S1Onv08oth7XjhC9NPQNiI3wAQJbpHzBq2t4mE+Wz0LGm7W3qH4jWAkg/wgcAZJkD7d1DRjwuZyT5/H060N5tX6eABBA+ACDLdPUMHzxG0w6wG+EDALJMqbMoqe0AuxE+ACDLzPGWyOMq0nAbai1d2vUyx1tiZ7eAuBE+ACDLFBZYamyokqQhAST0vrGhinofyFiEDwDIQnXVHm1aOktuV+TUittVpE1LZ1HnAxmNImMAkKXqqj1aWOWmwimyDuEDADLcSCXUCwss1UybnOYeAokhfABABqOEOnIRaz4AIENRQh25ivABABmIEurIZYQPADmhf8Bo37tn9dLRP2jfu2ez/qZMCXXkMtZ8AMh6ubgughLqyGWMfADIarm6LoIS6shlhA8AWSuRdRHZNi1DCXXkMqZdAGSteNdFbNx5SlsPdmTVtEyohPrKLYdlSREBixLqyHaMfADIWvGud/jb357KymkZSqgjVzHyASBrjWW9g9GlEYSm7W1aWOXO2BEESqgjFxE+AGSt0LqITn9f1HUfsVy+XTWTS5RTQh25hmkXAFkrnkfLx4PtqoC9CB8AstpI6yJ++PUZcX0H21UBezHtAiDrDbcuQpK2Hjw97LSMpUshhe2qgL0IHwBywnDrItiuCmQepl0A5DS2qwKZJ+HwsXv3bjU0NKi8vFyWZenFF1+M+Hz58uWyLCviNXfu3GT1FwASVlft0Z5HFug3K+bq53d/Rb9ZMVd7HllA8ADSJOFpl97eXs2cOVPf+9739O1vfztqm7q6Om3evDn8fvz48aPvIQAkAdtVgcyRcPior69XfX39iG0cDofcbveoOwUAAHJXStZ87Nq1S6WlpZoxY4ZWrFihrq6uYdsGg0EFAoGIFwAAyF1JDx/19fV65plntHPnTj355JM6ePCgFixYoGAwGLV9c3OzXC5X+FVRUZHsLgEAgAxiGWNG/Vxpy7L0wgsvaPHixcO28fl8qqys1NatW7VkyZIhnweDwYhgEggEVFFRIb/fr+Li4tF2DQAA2CgQCMjlcsV1/055nQ+Px6PKykqdOnUq6ucOh0MOhyPV3QCQBfoHDA9QA/JAysPH2bNn1dHRIY+HLW1AtkhHCNhxwqem7W3y+T97zorHVaTGhiq2xAI5JuHw8eGHH+qdd94Jv29vb9fRo0dVUlKikpISrV+/Xt/+9rfl8Xj0/vvv68c//rGmTJmib33rW0ntOIDUSEcI2HHCp5VbDg8pgd7p79PKLYcpBgbkmIQXnL755pu68cYbdeONN0qS1q5dqxtvvFF/9Vd/pcLCQh0/flyLFi3SjBkztGzZMs2YMUP79u2T0+lMeucBJFcoBFwePKTPQsCOE76k/2b/gFHT9raoz14JHWva3qb+gVEvTwOQYRIe+Zg/f75GWqP66quvjqlDANIjVgiwdCkELKxyJ3UK5kB795CwM/i3ff4+HWjvpkgYkCN4tgsASYmFgGTq6hn+N0fTDkDmI3wAkJS+EFDqLIrdKIF2ADIf4QOApPSFgDneEnlcRRpuIsfSpQWvc7wlSf1dAOlD+AAgKX0hoLDAUmNDVfg3Bv+mJDU2VFHvA8ghhA8AktIbAuqqPdq0dJbcrshRFberiG22QA4aU3n1VEikPCuA5LOrzke0QmaSqHAKZKmMKq8OILvUVXu0sMqd0hBANVMgvzHyAcBWw1UzDUUbplmA7JTI/Zs1HwBsQzVTABLhA4CN0lXIDEBmIXwAsA3VTAFIhA8ANqKaKQCJ8AHARlQzBSARPgDYKJ5CZnfffK3+9dgH2vfuWRaeAjmKrbYAbBetzsfVE8fJSDr/0cfhY9T+ALJHIvdvwgeAtLi8wun7Z3r1t789NaQNtT+A7EGdDwAZr7DAUs20yfrGl8u19WBH1DbU/gByE+EDQFpR+wPIP4QPAGlF7Q8g/xA+AKQVtT+A/MNTbQHY7vLFplOudMhd7NAfA8Goz3yxJLmp/QHkFMIHkIcuv/mXOi/d2AsLhiv9lVzRttle9ek2W0uKCCChHjU2VNnWPwCpR/gA8ky0m79d9TR2nPBp5ZbDQ0Y4/J/W9nBNHBdR58NNnQ8gJxE+gDwy3M2/09+nlVsOp7SeRv+AUdP2tqhTK6FRjwnjCvWL78/Smd6g7SMyAOzDglMgT8S6+UupracR75baggJLi77yOdVMm0zwAHIU4QPIE+mup8GWWgAhhA8gT6T75s+WWgAhhA8gT6T75j/HWyKPq2jI02xDLF1a+MqWWiD3ET6APJHum39hgaXGhqrwbw3+bYkttUC+IHwAeSITbv511R5tWjpLblfk6IrbVcSTa4E8YhljMupRkYk8khdA4tJZ5yMknUXOAKRGIvdvwgeQh7j5A0i2RO7fFBkD8lBhgaWaaZPT3Q0AeYo1HwAAwFaEDwAAYCvCBwAAsBXhAwAA2IrwAQAAbEX4AAAAtiJ8AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2InwAAABbET4AAICtCB8AAMBWhA8AAGArwgcAALBVwuFj9+7damhoUHl5uSzL0osvvhjxuTFG69evV3l5uSZMmKD58+fr5MmTyeovAADIcgmHj97eXs2cOVMbN26M+vkTTzyhDRs2aOPGjTp48KDcbrcWLlyonp6eMXcW2aF/wGjfu2f10tE/aN+7Z9U/YNLdJQBABrki0T+or69XfX191M+MMXrqqaf06KOPasmSJZKkX/3qVyorK9Ozzz6r++67b2y9RcbbccKnpu1t8vn7wsc8riI1NlSprtqTxp4lT/+A0YH2bnX19KnUWaQ53hIVFljp7hYAZI2Ew8dI2tvb1dnZqdra2vAxh8OhO+64Q3v37iV85LgdJ3xaueWwBo9zdPr7tHLLYW1aOivrA0g+hCsASLWkLjjt7OyUJJWVlUUcLysrC382WDAYVCAQiHgh+/QPGDVtbxsSPCSFjzVtb8vqKZhQuLo8eEifhasdJ3xD/oYpKAAYKqkjHyGWFTkEbYwZciykublZTU1NqegGbHSgvXvITflyRpLP36cD7d2qmTbZvo4lSaxwZelSuFpY5Q5PwTBKAgDRJXXkw+12S9KQUY6urq4hoyEh69atk9/vD786OjqS2SXYpKtn+OAxmnaZJpFwJY1ulAQA8kVSw4fX65Xb7VZLS0v42MWLF9Xa2qp58+ZF/RuHw6Hi4uKIF7JPqbMoqe0yTSLhKh+moABgLBKedvnwww/1zjvvhN+3t7fr6NGjKikp0bXXXqs1a9boscce0/Tp0zV9+nQ99thjmjhxou69996kdhyZZY63RB5XkTr9fVFvupYkt+vSzpBslEi4yvUpKAAYq4TDx5tvvqk777wz/H7t2rWSpGXLlumf//mf9fDDD+vChQt64IEHdO7cOd1yyy167bXX5HQ6k9drZJzCAkuNDVVaueWwLCkigIRW+zQ2VGXtltRzvcGYbTyfhqt/PfZBXN+ZrVNQADBWljEmo8Z+A4GAXC6X/H4/UzBZKBcXWfYPGN36s50jjmZI0pqvTZf3mkk60xPUT19+K+b3/mbFXEY+AOSMRO7fKdntgvxVV+3Rwip31hThiqdgWKxplJCn/v1U+N8FljTcko5sn4ICgLEifCDpCgusrPg/+nhHaUYzPTJS8JCyewoKAMaKp9oiLyWyFXYsO3QG5wu3qygnKr0CwFgw8oG8k2jBsFg7eUYyYKSf/Pl1muJ0ZPwUFADYhZEP5J1EC4aFdvJIn02bJGKK06FFX/mcaqZNJngAgAgfyEOjqcZaV+3RpqWz5HYlPgWTrYXVACBVmHZB3hltNdbBO3mmTHLoof/zO/0xkJuF1QAgVQgfyDrxbI8dyViqsQ7eybP+m7lbWA0AUoXwgaySjCJmyazGGpqOGdwnd5YXVgOAVKLCKbJGaHvs4As2FBES3cKazGqsYx2NAYBsl8j9m/CBrBCrxHloqmTPIwsSuukTGgAgOSivjpyTqifFZks1VgDIJWy1RVYYzfZYAEBmYuQDWSHR7bFMpwBA5iJ8ICvEU+L8qonjNDBg9MqxD/TTl99KykJSAEDyseAUGWe4UYvQbhdJCT9jZbQ7YgAA8WHBKbJWrO2v0WpqxCPaA+MAAOnBglNkjHgec19X7dGeRxbomR/coqsmjEvo+wc/MA4AkB6ED2SEWI+5ly6NWvQPGBUWWCqwLJ2/8PGofuu3bZ2j7icAYOwIH8gIiT7mfixbal84+gf1D2TUUicAyCuED2SEROt4jOUx9d29HzP1AgBpRPhARki0jkdo6+1ol41SjAwA0ofwgYwQChMj8Vz2mPvQk2kljSqAjGXkBAAwNoQPZITCAkvfnDly/Y1vzvREbJENbb11DwotI+2itRQZYgAA9qPOBzJC/4DRtt/5Rmyz7Xc+PVx33ZAAsrDKHVGU7FxvUKuePSIpshhZ6K8aG6qo8wEAaUT4gG0GVy6dXXm1Dv3+nLp6+nSmJxizcNhwT62N9mTaTQXWkGJkbkqsA0BGIHzAFtEqlxZYUqI7XuNdKBptRISHywFAZiB8IOVClUsH54zRlNpIZKFotBERAED6ET6QUiNVLk2EpUvTJiwUBYDsx24XpFSsyqXxYKEoAOQWRj6QUsko5sVCUQDILYQPpNRoi3n95M+v0xSng4WiAJCDCB9IqdmVV6tk0jh198b3BNrQ2o7lX/USOAAgRxE+kBSDa3jM8Zaopa1TTdvbEgoeEms7ACDXET6QkJFCxuULS6+aOE7nPxo5dAyu88HaDgDID4QPxC1aobDhQkas4DF50njteWSBjnacpwgYAOQZwgfiMlyhsFghYzhney/qaMd5ioABQB6izgdiSlahsMGSsQ0XAJB9GPnAsELrO/7jnTNjLhQWzZRJjqR/JwAg8xE+EFW09R1Jx/IOAMhLhA8MMdz6jmQ782Ewxb8AAMhErPlAhFSt74hmtNVPAQDZjZGPPDe4bseAMaOaapk4vlAfXewPvx9cw+NyPKEWAPIb4SOPRa3bMWHcqL7rwsV+/fDrM/T5KRNV6izSud6LWvXsYUmKGEWhiikAgPCRp4at23FhdHU7JGnrwdPa88iCcKjYVDBrSLihiikAgPCRQ6KVPo82upCKdR1Gks/fpwPt3eHCYXXVHi2scsfVJwBA/iB85IhoUyieYUYZDrR3p2wL7eDCYYUFFlVMAQAR2O2SA0JTKIMDRae/Tyu3HNaOE76I46msLMoOFgBALISPLDfSFEroWNP2NvVftvUkFQHB0qWRFnawAABiIXxkuVhTKJevxQiZ4y2Rx1UUs8BovCsz2MECAEgE4SPLxTuFcnm7wgJLjQ1VkoYGDOvT1323e+V2RY6QeFxFuu92rzyDjrtdRdq0dBY7WAAAcWHBaZaLdwplcLu6ao82LR15K+zDdddF3aky3HEAAOJB+MhyoSmUTn9f1HUfI1UTjbUVdridKuxgAQCMRdKnXdavXy/LsiJebrc72T+DT8WaQpFGXosRChKLvvI51UybzAgGACDlUrLm4/rrr5fP5wu/jh8/noqfwadCUyiD12iwFgMAkIlSMu1yxRVXMNphM6qJAgCyRUpGPk6dOqXy8nJ5vV7dfffdeu+994ZtGwwGFQgEIl4YncICS3O8JSp1Fqmr59L22v7hHi0LAECaJH3k45ZbbtGvf/1rzZgxQ3/84x/1N3/zN5o3b55OnjypyZOHLlJsbm5WU1NTsruRlxIpsQ4AQLpYxpiU/q9xb2+vpk2bpocfflhr164d8nkwGFQwGAy/DwQCqqiokN/vV3FxcSq7llOGe0ptaNKFtR8AgFQKBAJyuVxx3b9TvtV20qRJuuGGG3Tq1KmonzscDjkcjlR3I6fFKrFu6VKJ9YVVbtaAAADSLuUVToPBoN566y15PPxfd6qMpsQ6AADpkvTw8aMf/Uitra1qb2/Xf/7nf+o73/mOAoGAli1bluyfwqdGU2IdAIB0Sfq0y3/913/pnnvu0ZkzZ3TNNddo7ty52r9/vyorK5P9U/jUaEusAwCQDkkPH1u3bk32VyKGsZRYBwDAbjzVNsP1Dxjte/esXjr6B+1792zUuh1jLbEOAICdeLBcBkukbkc8T6kFACATpLzOR6IS2Seci/oHjA60d6ulrVP/6z/eH/J5rLodob+nxDoAwE4ZVecD8Ys20jFYrLodPO4eAJDpWPORIUIVSkcKHiHU7QAAZDPCRwYYqULpSKjbAQDIRoSPDBCrQulwqNsBAMhGrPnIAImOYFC3AwCQzRj5yACJjGBQtwMAkO0IHxkgVKE0nijhdhUNu80WAIBswLRLGl1ek+Pum6/VU7/9f7KkqAtPv//Vz+vrVW7qdgAAsh7hI02i1fS4auI4SdL5jz4OHxuuoikAANmK8JEGoZoeg0c4/B99LCPph1+frs9PmUSFUgBATiJ82Gykmh6h6qVbD3ZozyMLCB0AgJxE+BgknmejDNcmnr+NVdPj8uqllEkHAOQiwsdl4nmK7HBtvjnTo22/88V8Am28NT2oXgoAyFVstf3UcM9W6fT3aeWWw9pxwjdsG5+/T3+3u33Evw2Jt6YH1UsBALmKkQ/Ftw5j/baTkqyEnr8Sanv5E2hDNT06/X1Rv4vqpQCAXMfIh+Jbh9EZCKozMLqpkMufQFtYYKmxoUqShhQVo3opACAf5H346B8w+o93/pTy37k8uNRVe7Rp6Sy5XZFTK1QvBQDkg7yedom2eDRVuj8MRryvq/ZoYZU75u4YAAByTd6Gj+EKfaXKVRPGDTlWWGCxnRYAkHfyctplpAWmqXL+wsexGwEAkAfyMnzEWmCaCiVXOmz9PQAAMlVeho90FPByF1O3AwAAKU/Dh90FvDzU7QAAICwvw0eo0Feq95VYn76o2wEAwGfyMnyMVOgrEbH+lrodAAAMlbdbbUOFvkZb5+OHX5+urQc7Iv7WXezQPXOu1eenTKJuBwAAw7CMMXbuOI0pEAjI5XLJ7/eruLg45b938ZMBzW3+d3X3Xoz7bzyuIu15ZIEkUSQMAAAldv/O25GPkEO/P5dQ8Bi8hoMiYQAAJCYv13xcLpFttyWTxrGGAwCAMcr78DElgeJfP/nG9QQPAADGKK/Dx44TPj30v4/G3Z5CYQAAjF3ervlI9MFyFAoDACA58nLkI9EHy1EoDACA5MnLkY9EHizncRWpsaGKtR4AACRJXoaPeHe4rL5zmn648IuMeAAAkER5Oe0S74PlvvqFawgeAAAkWV6Gj9CD5UZy9cRxLDAFACAF8jJ8FBZY+ubMkddwnPvoY7W0ddrUIwAA8kdeho/+AaOXjvpitlu/7aT6BzLq0TcAAGS9vAwfB9q71RmIvei0MxDUgfZuG3oEAED+yMvwkcjzXBJpCwAAYsvL8FEycXzcbePdGQMAAOKTl+Hj/3YG4mp3paOAHS8AACRZXoaP33d/FFe7mypLqPMBAECS5V34eOWYT88f/kNcbW+bfk2KewMAQP7Jq/Lqza+06e92t8fVtsCSvlvz+dR2CACAPJQ3Ix+vHPsg7uAhSStu82r8FXlzegAAsE1ejHz0Dxj9z5dOxNXWkvQ/bvdq3Z9VpbZTAADkqbwIHwfau9Xd+3FcbZ/87zO1ZPbUFPcIAID8lbJ5haefflper1dFRUWaPXu23njjjVT9VEyJFArzXDUhhT0BAAApCR/PPfec1qxZo0cffVRHjhzRbbfdpvr6ep0+fToVPxdTvIXCJk8aT10PAABSLCXhY8OGDfr+97+vH/zgB7ruuuv01FNPqaKiQps2bUrFz8U0x1sijyt2APnpomrqegAAkGJJDx8XL17UoUOHVFtbG3G8trZWe/fuHdI+GAwqEAhEvJKtsMBSY0OVRooV993u1Z992ZP03wYAAJGSHj7OnDmj/v5+lZWVRRwvKytTZ2fnkPbNzc1yuVzhV0VFRbK7JElaWOXWmq/P0FUTxkUcL5k0Tk/feyO7WwAAsEnKdrtYVuQ4gzFmyDFJWrdundauXRt+HwgEkh5AdpzwqWl7m3z+zxaeXjVhnL731c9r9YLpTLUAAGCjpIePKVOmqLCwcMgoR1dX15DREElyOBxyOBzJ7kbYjhM+rdxyWGbQ8fMXPtZTvz2lL7qdqqtmugUAALskfdpl/Pjxmj17tlpaWiKOt7S0aN68ecn+uRH1Dxg1bW8bEjxCjKSm7W3qHxiuBQAASLaUTLusXbtW3/3ud3XTTTeppqZGf//3f6/Tp0/r/vvvT8XPDetAe3fEVEs0Pn+fDrR3q2baZJt6BQBAfktJ+Ljrrrt09uxZ/fVf/7V8Pp+qq6v1yiuvqLKyMhU/N6xO/4WktgMAAGOXsgWnDzzwgB544IFUfX1cznx4MantAADA2OX0Y1vPX4gvVMTbDgAAjF1Oh494N9Cy0RYAAPvkdPio+W9TktoOAACMXU6Hj7nTJuuqieNGbHPVxHGay04XAABsk9Pho7DA0uNLbhixzeNLbqDCKQAANsrp8CFJddUe/XLpLLmLI6uouosd+uXSWVQ3BQDAZinbaptJ6qo9Wljl1oH2bnX19KnUWaQ53hJGPAAASIO8CB/SpSkYqpgCAJB+OT/tAgAAMgvhAwAA2IrwAQAAbEX4AAAAtiJ8AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwVcZVODXGSJICgUCaewIAAOIVum+H7uMjybjw0dPTI0mqqKhIc08AAECienp65HK5RmxjmXgiio0GBgb0wQcfyOl0yrKS++C3QCCgiooKdXR0qLi4OKnfnUs4T/HjXMWH8xQ/zlV8OE/xsfM8GWPU09Oj8vJyFRSMvKoj40Y+CgoKNHXq1JT+RnFxMRdrHDhP8eNcxYfzFD/OVXw4T/Gx6zzFGvEIYcEpAACwFeEDAADYKq/Ch8PhUGNjoxwOR7q7ktE4T/HjXMWH8xQ/zlV8OE/xydTzlHELTgEAQG7Lq5EPAACQfoQPAABgK8IHAACwFeEDAADYKm/Cx9NPPy2v16uioiLNnj1bb7zxRrq7lHHWr18vy7IiXm63O93dygi7d+9WQ0ODysvLZVmWXnzxxYjPjTFav369ysvLNWHCBM2fP18nT55MT2fTKNZ5Wr58+ZBrbO7cuenpbBo1Nzfr5ptvltPpVGlpqRYvXqy33347og3XVHzniWvqkk2bNunLX/5yuJhYTU2N/u3f/i38eaZdT3kRPp577jmtWbNGjz76qI4cOaLbbrtN9fX1On36dLq7lnGuv/56+Xy+8Ov48ePp7lJG6O3t1cyZM7Vx48aonz/xxBPasGGDNm7cqIMHD8rtdmvhwoXhZxXli1jnSZLq6uoirrFXXnnFxh5mhtbWVq1atUr79+9XS0uLPvnkE9XW1qq3tzfchmsqvvMkcU1J0tSpU/X444/rzTff1JtvvqkFCxZo0aJF4YCRcdeTyQNz5swx999/f8SxL33pS+Yv//Iv09SjzNTY2GhmzpyZ7m5kPEnmhRdeCL8fGBgwbrfbPP744+FjfX19xuVymV/+8pdp6GFmGHyejDFm2bJlZtGiRWnpTybr6uoykkxra6sxhmtqOIPPkzFcUyO5+uqrzT/+4z9m5PWU8yMfFy9e1KFDh1RbWxtxvLa2Vnv37k1TrzLXqVOnVF5eLq/Xq7vvvlvvvfdeuruU8drb29XZ2RlxjTkcDt1xxx1cY1Hs2rVLpaWlmjFjhlasWKGurq50dynt/H6/JKmkpEQS19RwBp+nEK6pSP39/dq6dat6e3tVU1OTkddTzoePM2fOqL+/X2VlZRHHy8rK1NnZmaZeZaZbbrlFv/71r/Xqq6/qH/7hH9TZ2al58+bp7Nmz6e5aRgtdR1xjsdXX1+uZZ57Rzp079eSTT+rgwYNasGCBgsFguruWNsYYrV27Vrfeequqq6slcU1FE+08SVxTlzt+/LiuvPJKORwO3X///XrhhRdUVVWVkddTxj3VNlUsy4p4b4wZcizf1dfXh/99ww03qKamRtOmTdOvfvUrrV27No09yw5cY7Hddddd4X9XV1frpptuUmVlpV5++WUtWbIkjT1Ln9WrV+vYsWPas2fPkM+4pj4z3HnimvrMF7/4RR09elTnz5/Xv/zLv2jZsmVqbW0Nf55J11POj3xMmTJFhYWFQ9JdV1fXkBSISJMmTdINN9ygU6dOpbsrGS20I4hrLHEej0eVlZV5e409+OCD2rZtm15//XVNnTo1fJxrKtJw5ymafL6mxo8fry984Qu66aab1NzcrJkzZ+rnP/95Rl5POR8+xo8fr9mzZ6ulpSXieEtLi+bNm5emXmWHYDCot956Sx6PJ91dyWher1dutzviGrt48aJaW1u5xmI4e/asOjo68u4aM8Zo9erVev7557Vz5055vd6Iz7mmLol1nqLJ12sqGmOMgsFgZl5PaVnmarOtW7eacePGmX/6p38ybW1tZs2aNWbSpEnm/fffT3fXMspDDz1kdu3aZd577z2zf/9+841vfMM4nU7OkzGmp6fHHDlyxBw5csRIMhs2bDBHjhwxv//9740xxjz++OPG5XKZ559/3hw/ftzcc889xuPxmEAgkOae22uk89TT02Meeughs3fvXtPe3m5ef/11U1NTYz73uc/l3XlauXKlcblcZteuXcbn84VfH330UbgN11Ts88Q19Zl169aZ3bt3m/b2dnPs2DHz4x//2BQUFJjXXnvNGJN511NehA9jjPnFL35hKisrzfjx482sWbMitmrhkrvuust4PB4zbtw4U15ebpYsWWJOnjyZ7m5lhNdff91IGvJatmyZMebS1sjGxkbjdruNw+Ewt99+uzl+/Hh6O50GI52njz76yNTW1pprrrnGjBs3zlx77bVm2bJl5vTp0+nutu2inSNJZvPmzeE2XFOxzxPX1Gf+4i/+InyPu+aaa8zXvva1cPAwJvOuJ8sYY+wbZwEAAPku59d8AACAzEL4AAAAtiJ8AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2InwAAABbET4AAICt/j+QveQAMvWhxAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import Lasso\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.metrics import r2_score\n",
    "lasso=Lasso()\n",
    "lasso.fit(X_train_scaled,y_train)\n",
    "y_pred=lasso.predict(X_test_scaled)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)\n",
    "plt.scatter(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Cross Validation Lasso"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LassoCV(cv=5)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LassoCV</label><div class=\"sk-toggleable__content\"><pre>LassoCV(cv=5)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LassoCV(cv=5)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LassoCV\n",
    "lassocv=LassoCV(cv=5)\n",
    "lassocv.fit(X_train_scaled,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 0.6199701158263433\n",
      "R2 Score 0.9820946715928275\n"
     ]
    },
    {
     "data": {
      "image/png": "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Ghqizjc0NGjmzJkpalV6CAaDeuedd+T1elPdFEcrLy+Xx+OJesYuXLigxsZGnrFBtLe369SpU1n3jBljtGzZMr3wwgvasWOHysvLo17nmeox2H3qS7Y+U30xxigYDDrzeUrJNFebbd682YwYMcI888wzprm52dTW1poxY8aYEydOpLppjvLd737X7Ny507z//vtm37595m/+5m9Mfn4+98kY09HRYQ4fPmwOHz5sJJn169ebw4cPmw8++MAYY8zatWuN2+02L7zwgjly5Ii5++67jdfrNYFAIMUtt9dA96mjo8N897vfNXv27DEtLS3mjTfeMFVVVebaa6/Nuvu0ZMkS43a7zc6dO01ra2vkOHfuXOQanqnB7xPP1GdWrlxpdu3aZVpaWszbb79tvv/975ucnBzz2muvGWOc9zxlRfgwxpgnnnjClJWVmZEjR5opU6ZELdVCj7vuust4vV4zYsQIU1JSYu68805z7NixVDfLEd544w0jqdexcOFCY0zP0shVq1YZj8djXC6XufXWW82RI0dS2+gUGOg+nTt3zlRXV5trrrnGjBgxwlx33XVm4cKF5uTJk6lutu36ukeSzLPPPhu5hmdq8PvEM/WZb3/725HvuGuuucZ84xvfiAQPY5z3PFnGGGNfPwsAAMh2GT/nAwAAOAvhAwAA2IrwAQAAbEX4AAAAtiJ8AAAAWxE+AACArQgfAADAVoQPAABgK8IHAACwFeEDAADYivABAABsRfgAAAC2+v8uLd2PxG0diQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_pred=lassocv.predict(X_test_scaled)\n",
    "plt.scatter(y_test,y_pred)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Ridge Regression model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 0.5642305340105692\n",
      "R2 Score 0.9842993364555513\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7f30bd144e20>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import Ridge\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.metrics import r2_score\n",
    "ridge=Ridge()\n",
    "ridge.fit(X_train_scaled,y_train)\n",
    "y_pred=ridge.predict(X_test_scaled)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)\n",
    "plt.scatter(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 0.5642305340105692\n",
      "R2 Score 0.9842993364555513\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import RidgeCV\n",
    "ridgecv=RidgeCV(cv=5)\n",
    "ridgecv.fit(X_train_scaled,y_train)\n",
    "y_pred=ridgecv.predict(X_test_scaled)\n",
    "plt.scatter(y_test,y_pred)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'alpha_per_target': False,\n",
       " 'alphas': (0.1, 1.0, 10.0),\n",
       " 'cv': 5,\n",
       " 'fit_intercept': True,\n",
       " 'gcv_mode': None,\n",
       " 'scoring': None,\n",
       " 'store_cv_values': False}"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ridgecv.get_params()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Elasticnet Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 1.8822353634896005\n",
      "R2 Score 0.8753460589519703\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7f30bef239d0>"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import ElasticNet\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.metrics import r2_score\n",
    "elastic=ElasticNet()\n",
    "elastic.fit(X_train_scaled,y_train)\n",
    "y_pred=elastic.predict(X_test_scaled)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)\n",
    "plt.scatter(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error 0.6575946731430898\n",
      "R2 Score 0.9814217587854941\n"
     ]
    },
    {
     "data": {
      "image/png": "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53BPRXedJO4pSZowYYKefPJJffDBB/rggw80b948LViwIBwwbHc/mQwwY8YMc99990Xs++Y3v2n+4R/+IUktsqeamhozderUZDfD9iSZTZs2hV93d3cbj8djnnzyyfC+zs5O43a7zU9+8pMktNAeLr5OxhizZMkSs2DBgqS0x87a2tqMJNPY2GiM4Z7qz8XXyRjuqYFcdtll5he/+IUt76e07/k4d+6c9u7dq8rKyoj9lZWV2rFjR5JaZV9HjhxRYWGhSkpK9P3vf19//OMfk90k22tubpbP54u4x5xOp+bMmcM91odt27YpPz9fkydP1j333KO2trZkNynp/H6/JCkvL08S91R/Lr5OIdxTkbq6urRx40Z1dHSovLzclvdT2oeP48ePq6urSwUFBRH7CwoK5PP5ktQqe5o5c6b+/d//XW+//bZ+/vOfy+fzafbs2Tpx4kSym2ZrofuIe2xw8+fP169+9Stt3bpVzzzzjPbs2aN58+YpGAwmu2lJY4zRqlWrdPPNN6usrEwS91Rf+rpOEvfUhQ4cOKBLL71UTqdT9913nzZt2qTS0lJb3k+2W9U2URwOR8RrY0yvfZlu/vz54X+eMmWKysvLNXHiRL300ktatWpVEluWGrjHBnf77beH/7msrEw33HCDiouL9eabb2rRokVJbFnyrFixQh999JHef//9Xse4p77S33XinvrKVVddpf379+uLL77Qb37zGy1ZskSNjY3h43a6n9K+52PcuHHKzs7ule7a2tp6pUBEGjNmjKZMmaIjR44kuym2FpoRxD0WO6/Xq+Li4oy9xx544AG98cYbevfddzVhwoTwfu6pSP1dp75k8j01cuRIXXnllbrhhhtUW1urqVOn6tlnn7Xl/ZT24WPkyJGaPn26GhoaIvY3NDRo9uzZSWpVaggGg/r444/l9XqT3RRbKykpkcfjibjHzp07p8bGRu6xQZw4cUItLS0Zd48ZY7RixQq9+uqr2rp1q0pKSiKOc0/1GOw69SVT76m+GGMUDAbteT8lZZirxTZu3GhGjBhhfvnLX5qmpiazcuVKM2bMGHP06NFkN81WHnzwQbNt2zbzxz/+0ezatct85zvfMS6Xi+tkjGlvbzf79u0z+/btM5LM+vXrzb59+8ynn35qjDHmySefNG6327z66qvmwIED5o477jBer9cEAoEkt9xaA12n9vZ28+CDD5odO3aY5uZm8+6775ry8nJz+eWXZ9x1WrZsmXG73Wbbtm2mtbU1vJ05cyZ8DvfU4NeJe+orq1evNtu3bzfNzc3mo48+Mo8++qjJysoy77zzjjHGfvdTRoQPY4z58Y9/bIqLi83IkSPNtGnTIqZqocftt99uvF6vGTFihCksLDSLFi0yhw4dSnazbOHdd981knptS5YsMcb0TI2sqakxHo/HOJ1Oc+utt5oDBw4kt9FJMNB1OnPmjKmsrDTjx483I0aMMFdccYVZsmSJOXbsWLKbbbm+rpEk88ILL4TP4Z4a/DpxT33l7rvvDv/GjR8/3nzrW98KBw9j7Hc/OYwxxrp+FgAAkOnSfswHAACwF8IHAACwFOEDAABYivABAAAsRfgAAACWInwAAABLET4AAIClCB8AAMBShA8AAGApwgcAALAU4QMAAFiK8AEAACz1/wFqTCw0diEQwgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import ElasticNetCV\n",
    "elasticcv=ElasticNetCV(cv=5)\n",
    "elasticcv.fit(X_train_scaled,y_train)\n",
    "y_pred=elasticcv.predict(X_test_scaled)\n",
    "plt.scatter(y_test,y_pred)\n",
    "mae=mean_absolute_error(y_test,y_pred)\n",
    "score=r2_score(y_test,y_pred)\n",
    "print(\"Mean absolute error\", mae)\n",
    "print(\"R2 Score\", score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "elasticcv.alphas_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
