
# A.I. Bot for racing game

A reinforcement learning model based on PPO algorithm. 


## Installation

### swig
Download swig file from https://www.swig.org/Doc1.3/Windows.html 
extract and add the path of the swig file in environment variable.

### Libraries
Install python liraries:

1. gym 
```bash
pip install gym[all]
```
2. stable-baselines
```bash
pip install stable-baselines[extra]
```
3. pyglet
```bash
pip install pyglet
```
4. Box2D
```bash
pip install Box2D
```
5. swig
```bash
pip install swig
```

## API 

The Gym API's API models environments as simple Python ```env``` classes. Creating environment instances and interacting with them is very simple- here's an example using the "CartPole-v1" environment:
```python
import gym
env = gym.make("CartPole-v1")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()
```



## Learn More
To learn more about gym, environment and PPO algorithm, take a look at following resources

[Gym Documentation](https://www.gymlibrary.dev/content/basic_usage/) - Learn about gym and its API's.

[Box2D Environment](https://www.gymlibrary.dev/environments/box2d/) - Learn about the various Box2D environments.

[PPO Algorithm](https://openai.com/blog/openai-baselines-ppo/) - A brief description about PPO algorithm and its baselines