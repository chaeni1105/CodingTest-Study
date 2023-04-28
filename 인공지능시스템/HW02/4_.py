import pandas as pd 
import numpy as np
pd_data = pd.read_csv('./train_data.csv') # train_data.csv 파일 읽어 오기

features = pd_data.iloc[:100, :-1] # 100개의 데이터만 선택,  features 변수에 할당
target = pd_data.iloc[:100, -1:] # # 100개의 레이블만 선택, target 변수에 할당

def entropy(y): # 엔트로피 계산 함수 정의
    # y에 있는 클래스 레이블들의 엔트로피를 계산합니다.
    value, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

def information_gain(X, y, feature_idx): # 정보 이득 계산 함수 정의
    # feature_idx에 해당하는 특징을 사용하여 분할했을 때의 정보 이득을 계산합니다.
    parent_entropy = entropy(y)
    values, counts = np.unique(X.iloc[:, feature_idx], return_counts=True)
    child_entropy = 0
    for value, count in zip(values, counts):
        child_y = y[X.iloc[:, feature_idx] == value]
        child_entropy += count / len(X) * entropy(child_y)
    ig = parent_entropy - child_entropy
    return ig

def find_best_feature(X, y): # 가장 정보 이득이 큰 특징을 찾는 함수 정의
    # 모든 특징들 중에서 가장 정보 이득이 큰 특징을 찾아 반환합니다.
    best_feature = None
    best_ig = 0
    for i in range(X.shape[1]):
        ig = information_gain(X, y, i)
        if ig > best_ig:
            best_feature = i
            best_ig = ig
    return best_feature

def build_tree(X, y): # Decision tree를 구성하는 함수 정의
    # 재귀적으로 decision tree를 구성합니다.
    # Base case: 모든 레이블이 동일한 경우
    if len(np.unique(y)) == 1:
        return y.iloc[0]
    # 먼저 base case를 처리하고, 더 이상 분할할 특징이 없을 때, 데이터의 가장 많은 레이블을 반환
    if X.shape[1] == 0:
        return np.bincount(y).argmax()
    # recursive case에서는 find_best_feature 함수를 사용하여 가장 정보 이득이 큰 특징을 찾고, 그 특징의 값을 기준으로 데이터를 분할합니다.
    best_feature = find_best_feature(X, y)
    tree = {best_feature: {}}
    values = np.unique(X.iloc[:, best_feature])
    for value in values:
        index = X.iloc[:, best_feature] == value
        subtree = build_tree(X.loc[index], y.loc[index])
        tree[best_feature][value] = subtree
    return tree

tree = build_tree(features, target) # 트리 만들기
print(tree) # 학습된 Decision tree를 출력