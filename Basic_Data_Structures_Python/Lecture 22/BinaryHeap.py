# max heap
def upheapify(heap, idx):
	if idx == 0:
		return
	pi = (idx - 1) // 2
	if heap[pi] < heap[idx]:
		temp = heap[pi]
		heap[pi] = heap[idx]
		heap[idx] = temp
		upheapify(heap, pi)
	else:
		return


def downheapify(heap, idx):
	lc = 2*idx + 1
	rc = 2*idx + 2

	if lc >= len(heap) and rc >= len(heap):
		return
	largest = idx
	if lc < len(heap) and heap[lc] > heap[largest]:
		largest = lc
	if rc < len(heap) and heap[rc] > heap[largest]:
		largest = rc
	if largest == idx:
		return
	temp = heap[largest]
	heap[largest] = heap[idx]
	heap[idx] = temp
	downheapify(heap, largest)

def insert(heap, key):
	heap.append(key)
	upheapify(heap, len(heap)-1)

def get(heap):
	return heap[0]

def removepeek(heap):
	i = len(heap) - 1
	temp = heap[0]
	heap[0] = heap[i]
	heap[i] = temp
	heap.pop()
	downheapify(heap, 0)

def buildheap(heap):
	i = len(heap) - 1
	i = (i // 2) + 1
	while i >= 0:
		downheapify(heap, i)
		i -= 1
	return

# heap = []
# n = int(input())
# while n > 0:
# 	n -=1
# 	x = int(input())
# 	insert(heap, x)

# print(heap)

heap = [int(x) for x in input().split()]
buildheap(heap)
print(heap)
