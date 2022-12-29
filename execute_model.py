import model
import os
from stable_baselines3 import PPO
from model import env
from stable_baselines3.common.evaluation import evaluate_policy


ppo_path = os.path.join('Training','saved_model','model_400k')
model = PPO.load(ppo_path, env)
evaluate_policy(model, env, n_eval_episodes=2, render=True)