# -*- coding: utf-8 -*-
import subprocess, os

class Maxsat_Solver:
    def __init__(self, wcnf_fname = "test.wcnf"):
        """
            Input: a wcnf file name
            This class contains some Maxsat_Solver, for this time, I just use OpenWBO
            This class can be expanded in the future for more SAT solver
        """
        ## The wcnf file name that will be used for the OpenWBO
        self.CNF_fname = wcnf_fname
        
        # self.SAT_Solver = "OpenWBO"
        
        ## cmdline of OpenWBO, -algorthm=5 represents that the OpenWBO will choose the best algrithm by OpenWBO self 
        self.openwbo_cmdline = ["./open-wbo", "-algorithm=5" "-weight-strategy=2", self.CNF_fname]
        
        ## Used for read and write OpenWBO output
        self.openwbp_solution = ""
        self.solution=[]
        self.openwbo_out_fname = "solver.out"
        
        ## other output parameters
        self.weight_type = []
        self.runtime = ""
        self.hard_clause_num = 0
        self.soft_clause_num = 0
        self.unsat_budget = 0
        self.optimum=False
        self.solved=True
    
    def _run_openwbo_solver(self):
        """
            run openWBO in OS
        """
        out_file=open( self.openwbo_out_fname, "w")
        child = subprocess.Popen( self.openwbo_cmdline, stdout=out_file)
        child.wait()
        out_file.flush()
        out_file.close()
        
    def _read_result(self):
        """
            get the results from SAT Solver, current this just OpenWBO
        """
        ## if self.SAT_Solver == "OpenWBO":
        out_file=open( self.openwbo_out_fname, "r")
        while 1:
            line = out_file.readline()
            if line=='':
                break
            elif line.startswith("v "):
                self.openwbp_solution =line[2:].rstrip()
            elif line.startswith("s UNSATISFIABLE"):
                self.solved=False
                out_file.close()
                break
            elif line.startswith("c |  Problem Type"):
                self.weight_type=line[18:-1].rstrip().lstrip()
            elif line.startswith("c |  Parse time:"):
                self.weight_type=line[16:-2].rstrip().lstrip()
            elif line.startswith("c |  Number of hard clauses:"):
                self.hard_clause_num=int(line[28:-2].rstrip().lstrip())
            elif line.startswith("c |  Number of soft clauses:"):
                self.soft_clause_num=int(line[28:-2].rstrip().lstrip())
            elif line.startswith("o "):
                self.unsat_budget=int(line[2:].rstrip().lstrip())
            elif line.startswith("s OPTIMUM FOUND"):
                self.Optimum=True
            else:
                pass
        out_file.flush()
        out_file.close()
        
    def _build_solution(self):
        self.solution=[]
        for i in self.openwbp_solution.split(" "):
            if i.startswith("-"):
                self.solution.append(False)
            else:
                self.solution.append(True)
                
    def delete_out_file(self):
        """
            delete the tmp file used, for debug, I set this method
        """
        ## if self.SAT_Solver == "OpenWBO":
        os.remove(self.openwbo_out_fname)
        os.remove(self.CNF_fname)
    
    def solve(self):
        """
            solver method, final step
        """
        ## if self.SAT_Solver == "OpenWBO":
        self._run_openwbo_solver()
        self._read_result()
        self._build_solution()