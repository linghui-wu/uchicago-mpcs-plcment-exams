import sys


def dfs(graph, root_vertex):
    visit[root_vertex] = 1

    for i in graph:
        if (root_vertex == i[0]) & (visit[i[1]] != 1):
            visit[i[1]] = 1
            dfs(graph, i[1])
        elif (root_vertex == i[1]) & (visit[i[0]] != 1):
            visit[i[0]] = 1
            dfs(graph, i[0])
    # return 0


def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    v_num = int(contents[0])
    e_num = int(contents[1])

    graph = []
    for i in contents[2:]:
        graph.append([int(i.split(' ')[0]), int(i.split(' ')[1].rstrip('\n'))])
    # print(graph)

    global visit
    visit = [0 for i in range(v_num)]

    count = 0
    for i in range(v_num):
        if visit[i] == 0:
            count += 1
            dfs(graph, i)

    print(count)

if __name__ == '__main__':
    main()