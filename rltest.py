from returnmatrix import returnmatrix
from bound import bound
import matplotlib.pyplot as plt
import numpy as np


# print entire array
# np.set_printoptions(threshold=np.nan)


filename = 'gridworld-bridge.png'
sz = (22, 18)


start = [sz[0] - 1, np.arange(4, 8)]
finish = [0, np.arange(10, 14)]

# docs:
# http://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.size
im = returnmatrix(filename, sz, start, finish)

# initialize agent (row, col[, step])
alpha = .1
gamma = .95
Q = np.zeros(sz + (4,))
Qsave = Q.copy()
target_pol = 4 * np.ones(sz)
Action_set = np.array([[1, 0], [0, -1], [-1, 0], [0, 1]]).T


tolerance = .001
count = 0
converging = True
while converging:
    pos = np.array([start[0], np.random.choice(start[1])])
    action = np.random.randint(4)
    step = Action_set.dot(np.arange(4) == action)
    R = 0

    SA = tuple(pos) + (action,)

    (_, S2) = bound(im, pos, pos + step)

    Q[SA] = Q[SA] + alpha * (R + gamma * np.max(Q[S2]) - Q[SA])

    episode_in_progress = True
    while episode_in_progress:
        pos = S2
        S = tuple(pos)
        action = np.random.randint(4)
        step = Action_set.dot(np.arange(4) == action)

        SA = S + (action,)

        (episode_in_progress, S2) = bound(im, pos, pos + step)
        R = not episode_in_progress

        Q[SA] = Q[SA] + alpha * \
            (R + gamma * np.max(Q[S2[0], S2[1], :]) - Q[SA])

        target_pol[S] = np.argmax(Q[S[0], S[1], :])

    count += 1
    if count % 250 == 0:
        print('entered check')
        err = np.max(np.abs(Q - Qsave).ravel())
        print('err =', err)
        if err < tolerance:
            converging = False
        else:
            Qsave = Q.copy()


plt.imshow(target_pol)
plt.show()
