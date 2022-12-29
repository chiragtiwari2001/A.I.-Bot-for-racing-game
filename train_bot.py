from model import model_name
import gym
import os
from model import env
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# training the model
env = gym.make(model_name)
env = DummyVecEnv([lambda: env])
log_path = os.path.join('Training', 'Logs')
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=log_path)
model.learn(total_timesteps=1500000)

# saving the model
ppo_path = os.path.join('Training','saved_model','model_1.5M')
model.save(ppo_path)
