import heapq

class JobScheduler:
    def __init__(self):
        """Initializes an empty list to act as our Max Heap."""
        self.heap = []

    def insert_job(self, priority: int, job_name: str):
        """a) Insert a job into the scheduler."""
        heapq.heappush(self.heap, (-priority, job_name))
        print(f"\n[Success] Inserted Job: '{job_name}' with Priority {priority}")

    def delete_highest_priority(self):
        """b) Delete (and process) the job with the highest priority."""
        if not self.heap:
            print("\n[Notice] Scheduler is empty. No jobs to process.")
            return None
       
        neg_priority, job_name = heapq.heappop(self.heap)
        actual_priority = -neg_priority
        print(f"\n[Processed & Deleted] Job: '{job_name}' (Priority {actual_priority})")
        return job_name

    def peek_highest_priority(self):
        """c) Peek at the job with the highest priority without removing it."""
        if not self.heap:
            print("\n[Notice] Scheduler is empty.")
            return None
       
        neg_priority, job_name = self.heap[0]
        actual_priority = -neg_priority
        print(f"\n[Next Job] Name: '{job_name}' | Priority: {actual_priority}")
        return (job_name, actual_priority)

    def display_jobs(self):
        """d) Display all jobs currently in the heap order."""
        if not self.heap:
            print("\n[Notice] Scheduler is empty.")
            return
       
        print("\n--- Current Jobs in Heap Order ---")
        for neg_priority, job_name in self.heap:
            print(f"   [Priority: {-neg_priority}] -> Job: {job_name}")
        print("-" * 35)


if __name__ == "__main__":
    scheduler = JobScheduler()
   
    while True:
        print("\n=== MAX HEAP JOB SCHEDULER ===")
        print("1. Insert a job")
        print("2. Delete highest priority job")
        print("3. Peek at highest priority job")
        print("4. Display all jobs")
        print("5. Exit")
       
        choice = input("Enter your choice (1-5): ").strip()
       
        if choice == '1':
            job_name = input("Enter job name: ").strip()
            try:
                priority = int(input("Enter job priority (integer): ").strip())
                scheduler.insert_job(priority, job_name)
            except ValueError:
                print("\n[Error] Invalid priority! Please enter a valid integer.")
               
        elif choice == '2':
            scheduler.delete_highest_priority()
           
        elif choice == '3':
            scheduler.peek_highest_priority()
           
        elif choice == '4':
            scheduler.display_jobs()
           
        elif choice == '5':
            print("\nExiting Job Scheduler. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice! Please enter a number between 1 and 5.")
