#!/usr/bin/env python3

# The input is a list of job start times (in ms).
# Each job takes 1000ms to execute.
# Jobs are served by a list of servers.
#
# What is the minimum number of servers necessary to serve all jobs as they
# arrive? That is, none of the jobs is required to wait for a server.

# Standard input is a sequence of integers, one per line, terminated by a line
# containing only the text "end".

# For each server in the list servers, servers[i] is the next time
# at which servers[i] is available to accept new jobs.
#
servers = []
duration = 1000

line = input()
while line != "end":
   start_time = int(line)

   # Search for a free server at time start_time.
   #
   i = 0
   while i < len(servers) and start_time < servers[i]:
      i += 1

   if i < len(servers):
      # Reallocate an existing server i.
      #
      # It will next be free to accept new jobs at time
      # start_time + duration.
      servers[i] = start_time + duration
   else:
      # Allocate a new server.
      #
      # It will next be free to accept new jobs at time
      # start_time + duration.
      servers.append(start_time + duration)

   line = input()

print(len(servers))
