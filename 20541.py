import sys
import bisect

input = sys.stdin.readline

class Album:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.albums = {}  # 앨범을 dict로 관리
        self.album_names = []  # 앨범 이름들을 정렬된 상태로 유지
        self.pictures = set()  # 사진은 set으로 관리
        self.picture_names = []  # 사진 이름들을 정렬된 상태로 유지

root: Album = Album("album", None)
root.parent = root
cur: Album = root

for i in range(int(input())):
    cmd = input().split()

    if cmd[0] == "mkalb":
        if cmd[1] in cur.albums:
            print("duplicated album name")
        else:
            cur.albums[cmd[1]] = Album(cmd[1], cur)
            bisect.insort(cur.album_names, cmd[1])  # 앨범 이름을 정렬된 리스트에 삽입

    elif cmd[0] == "rmalb":
        album_cnt = 0
        picture_cnt = 0
        target = []
        if cur.album_names:
            if cmd[1] == '-1':
                # 사전순으로 가장 빠른 앨범 삭제
                name = cur.album_names.pop(0)
                target.append(cur.albums.pop(name))
                album_cnt += 1
            elif cmd[1] == '0':
                # 모든 앨범 삭제
                album_cnt += len(cur.albums)
                target.extend(cur.albums.values())
                cur.albums.clear()
                cur.album_names.clear()
            elif cmd[1] == '1':
                # 사전순으로 가장 늦은 앨범 삭제
                name = cur.album_names.pop()
                target.append(cur.albums.pop(name))
                album_cnt += 1
            elif cmd[1] in cur.albums:
                # 특정 앨범 삭제
                name = cmd[1]
                cur.album_names.remove(name)
                target.append(cur.albums.pop(name))
                album_cnt += 1

        while target:
            next_album = target.pop()
            album_cnt += len(next_album.albums)
            picture_cnt += len(next_album.pictures)
            target.extend(next_album.albums.values())
        print(album_cnt, picture_cnt)

    elif cmd[0] == 'insert':
        if cmd[1] in cur.pictures:
            print("duplicated photo name")
        else:
            cur.pictures.add(cmd[1])
            bisect.insort(cur.picture_names, cmd[1])  # 사진 이름을 정렬된 리스트에 삽입

    elif cmd[0] == 'delete':
        picture_cnt = 0
        if cur.picture_names:
            if cmd[1] == '-1':
                # 사전순으로 가장 빠른 사진 삭제
                t = cur.picture_names.pop(0)
                cur.pictures.remove(t)
                picture_cnt += 1
            elif cmd[1] == '0':
                # 모든 사진 삭제
                picture_cnt += len(cur.pictures)
                cur.pictures.clear()
                cur.picture_names.clear()
            elif cmd[1] == '1':
                # 사전순으로 가장 늦은 사진 삭제
                t = cur.picture_names.pop()
                cur.pictures.remove(t)
                picture_cnt += 1
            elif cmd[1] in cur.pictures:
                # 특정 사진 삭제
                cur.picture_names.remove(cmd[1])
                cur.pictures.remove(cmd[1])
                picture_cnt += 1
        print(picture_cnt)

    elif cmd[0] == 'ca':
        if cmd[1] == '..':
            cur = cur.parent
        elif cmd[1] == '/':
            cur = root
        elif cmd[1] in cur.albums:
            cur = cur.albums[cmd[1]]
        print(cur.name)
