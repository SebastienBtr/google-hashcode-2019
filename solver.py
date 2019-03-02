import sys


class Photo:
    def __init__(self, id, tags):
        self.id = id
        self.tags = tags

    def display(self):
        print(" " + str(self.id) + " " + str(self.tags))


def readfile(path):
    horiz = []
    vertiz = []
    file = open(path, 'r')
    lines = [line.rstrip('\n') for line in file]

    for i in range(1, len(lines)):
        line = line = lines[i].split(' ')
        tags = []

        # recup les tags
        for j in range(2, len(line)):
            tags.append(line[j])

        photo = Photo(i-1, tags)

        if line[0] == "H":
            horiz.append(photo)
        else:
            vertiz.append(photo)

    mergedVertiz = mergeVertiz(vertiz)
    tablito = mergedVertiz + horiz

    print(len(tablito))
    solve(tablito)


def mergeVertiz(vertiz):
    photos = []

    for i in range(0, len(vertiz) - 1, 2):

            newPhoto = Photo(str(vertiz[i].id) + " " + str(vertiz[i + 1].id),
                            set(vertiz[i].tags) | set(vertiz[i + 1].tags))

            photos.append(newPhoto)

    return photos


def solve(lstPhoto):
    print("Go Solve !")

    resul = []

    photocourante = lstPhoto[0]

    while len(lstPhoto) > 1:

        lstPhoto.remove(photocourante)
        nextPhoto = None
        min = 0
        photocouranteTags = set(photocourante.tags)

        for tag in photocourante.tags:

            match = searchMatchingPhoto(lstPhoto, tag)

            if(match != None):
                tagsSet = photocouranteTags | set(match.tags)

                if nextPhoto == None:
                    nextPhoto = match
                    min = len(tagsSet)

                elif len(tagsSet) < min:
                    nextPhoto = match
                    min = len(tagsSet)
                    

        if nextPhoto == None:
            photocourante = lstPhoto[0]
        else:
            resul.append(str(photocourante.id))
            photocourante = nextPhoto

        #last photo
        if len(lstPhoto) == 1:
            resul.append(str(photocourante.id))

    print("#######")
    for line in resul:
        print(line)

    writeResul(resul)


def searchMatchingPhoto(lstPhoto, searchedTag):
    for photo in lstPhoto:
        for tag in photo.tags:
            if(tag == searchedTag):
                return photo
    return None


def writeResul(resul):
    nbResul = len(resul)
    file = open("output", "w")
    file.write(str(nbResul)+"\n")

    for photo in resul:
        file.write(photo+"\n")

    file.close()


readfile(sys.argv[1])
