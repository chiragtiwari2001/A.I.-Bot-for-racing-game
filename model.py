import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

model_name = 'CarRacing-v1'
env = gym.make(model_name)

env.reset()
env.action_space
env.observation_space

episode = 2

for episode in range(1, episode+1):
    obs = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        score += reward

    print('Episode:{}, Score:{}'.format(episode, score))
