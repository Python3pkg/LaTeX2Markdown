test = r"""% Created by Andrew Tulloch

%!TEX TS-program = xelatex
%!TEX encoding = UTF-8 Unicode


\documentclass[12pt]{amsart}
\usepackage{amsthm, amsmath, amssymb}
\usepackage{geometry, setspace, graphicx, enumerate, fullpage}
\onehalfspacing                 
\usepackage{fontspec,xltxtra,xunicode}


% AMS Theorems
\theoremstyle{plain}% default 
\newtheorem{thm}{Theorem}[section] 
\newtheorem{lem}[thm]{Lemma} 
\newtheorem{prop}[thm]{Proposition} 
\newtheorem{exer}[thm]{Exercise} 

\newtheorem*{cor}{Corollary} 


\newcommand{\res}[2]{\text{Res}(#1,#2)}
\theoremstyle{definition} 
\newtheorem{defn}[thm]{Definition}
\newtheorem{conj}[thm]{Conjecture}
\newtheorem{exmp}[thm]{Example}

\theoremstyle{remark} 
\newtheorem*{rem}{Remark} 
\newtheorem*{note}{Note} 
\newtheorem{case}{Case} 

\newcommand{\expc}[1]{\mathbb{E}\left[#1\right]}
\newcommand{\var}{\text{Var}}
\newcommand{\cov}[1]{\text{Cov}\left(#1\right)}
\newcommand{\prob}[1]{\mathbb{P}(#1)}
\newcommand{\given}{ \, | \,}
\newcommand{\us}{0 \leq u \leq s}
\newcommand{\ts}[1]{\{ #1 \}}

\renewcommand{\phi}{\varphi}
\newcommand{\sigf}{\mathcal{F}}

\newcommand{\dzz}{\, dz}
\newcommand{\bigo}[1]{\mathcal{O}(#1)}

\newcommand{\al}{\alpha}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\N}{\mathbb{N}}

\newcommand{\I}{\mathbb{I}}

\renewcommand{\P}{\mathbb{P}}

\newcommand{\F}{\mathbb{F}}
\newcommand{\Ga}{\mathbb{G}}

\newcommand{\aut}[1]{\text{Aut}{(#1)}}

\newcommand{\gener}[1]{\langle #1 \rangle}
\newcommand{\charr}[1]{\text{char}(#1)}
\newcommand{\nth}{n\textsuperscript{th}}

\newcommand{\tworow}[2]{\genfrac{}{}{0pt}{}{#1}{#2}}
\newcommand{\xdeg}[2]{[#1 : #2]}
\newcommand{\gal}[2]{\text{Gal}(#1/#2)}
\newcommand{\minpoly}[2]{m_{#1, #2}(x)}

\newcommand{\mapping}[5]{\begin{align*}
	#1 : \quad     #2 &\rightarrow #3 \\
			#4  &\mapsto #5
\end{align*}	
}


\def\cip{\,{\buildrel p \over \rightarrow}\,} 
\def\cid{\,{\buildrel d \over \rightarrow}\,} 
\def\cas{\,{\buildrel a.s. \over \rightarrow}\,} 

\def\clp{\,{\buildrel L^p \over \rightarrow}\,} 

\def\eqd{\,{\buildrel d \over =}\,} 
\def\eqas{\,{\buildrel a.s. \over =}\,}

\newcommand{\sigg}{\mathcal{G}}		
\newcommand{\indic}[1]{\mathbf{1}_{\{ #1 \}} }
\newcommand{\itos}{\text{It\^o's\ }}
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}

		
		
\title{Elements of Statistical Learning - Chapter Solutions}								% Document Title
\author{Andrew Tulloch}


\begin{document}
\maketitle
\section{Chapter 1}

No exercises.

\section{Chapter 2}
\begin{exer}
    Suppose that each of $K$-classes has an associated target $t_k$, which is a vector of all zeroes, except a one in the $k$-th position.  Show that classifying the largest element of $\hat y$ amounts to choosing the closest target, $\min_k \| t_k - \hat y \|$ if the elements of $\hat y$ sum to one. 
\end{exer}
\begin{proof}
    The assertion is equivalent to showing that \[
    \argmax_i \hat y_i = \argmin_k \| t_k - \hat y \| = \argmin_k \|\hat y - t_k \|^2
\] by monotonicity of $x \mapsto x^2$ and symmetry of the norm.  

WLOG, let $\| \cdot \|$ be the Euclidean norm $\| \cdot \|_2$.  Let $k = \argmax_i \hat y_i$, with $\hat y_k = \max y_i$.  Note that then $\hat y_k \geq \frac{1}{K}$, since $\sum \hat y_i = 1$.   

Then for any $k' \neq k$ (note that $y_{k'} \leq y_k$), we have \begin{align*}
    \| y - t_{k'} \|_2^2 - \| y - t_k \|_2^2 &= y_k^2 + \left(y_{k'} - 1 \right)^2 - \left( y_{k'}^2 + \left(y_k - 1 \right)^2 \right) \\
    &= 2 \left(y_k - y_{k'}\right) \\
    &\geq 0
\end{align*} since $y_{k'} \leq y_k$ by assumption.

Thus we must have \[
    \argmin_k \| t_k - \hat y \| = \argmax_i \hat y_i
\] as required.    
\end{proof}

\begin{exer}
    Show how to compute the Bayes decision boundary for the simulation example in Figure 2.5.
\end{exer}
\begin{proof}
    The Bayes classifier is \[
        \hat G(X) = \argmax_{g \in \mathcal G} P(g | X = x ).
    \] In our two-class example $\textsc{orange}$ and $\textsc{blue}$, the decision boundary is the set where \[
        P(g=\textsc{blue} | X = x) = P(g =\textsc{orange} | X = x) = \frac{1}{2}.
    \]  
    
    By the Bayes rule, this is equivalent to the set of points where \[
        P(X = x | g = \textsc{blue}) P(g = \textsc{blue}) = P(X = x | g = \textsc{orange}) P(g = \textsc{orange})
    \] And since we know $P(g)$ and $P(X=x|g)$, the decision boundary can be calculated.
\end{proof}
    
\begin{exer}
    Consider $N$ data points uniformly distributed in a $p$-dimensional unit ball centered at the origin.  Show the the median distance from the origin to the closest data point is given by \[
        d(p, N) = \left(1-\left(\frac{1}{2}\right)^{1/N}\right)^{1/p}
    \] 
\end{exer}
\begin{proof}
    Let $r$ be the median distance from the origin to the closest data point.  Then \[
        P(\text{All $N$ points are further than $r$ from the origin}) = \frac{1}{2}
    \] by definition of the median.

    Since the points $x_i$ are independently distributed, this implies that \[
        \frac{1}{2} = \prod_{i=1}^N P(\|x_i\| > r)
    \] and as the points $x_i$ are uniformly distributed in the unit ball, we have that \begin{align*}
        P(\| x_i \| > r) &= 1 - P(\| x_i \| \leq r) \\
                         &= 1 - \frac{Kr^p}{K} \\
                         &= 1 - r^p
    \end{align*}  Putting these together, we obtain that \[
        \frac{1}{2} = \left(1-r^p \right)^{N}
    \] and solving for $r$, we have \[
        r = \left(1-\left(\frac{1}{2}\right)^{1/N}\right)^{1/p}
    \]
\end{proof}

\begin{exer}
    Consider inputs drawn from a spherical multivariate-normal distribution $X \sim N(0,\mathbf{1}_p)$. The squared distance from any sample point to the origin has a $\chi^2_p$ distribution with mean $p$. Consider a prediction point $x_0$ drawn from this distribution, and let $a = \frac{x_0}{\| x_0\|}$ be an associated unit vector. Let $z_i = a^T x_i$ be the projection of each of the training points on this direction.
    Show that the $z_i$ are distributed $N(0,1)$ with expected squared distance from the origin 1, while the target point has expected squared distance $p$ from the origin.
    Hence for $p = 10$, a randomly drawn test point is about 3.1 standard deviations from the origin, while all the training points are on average one standard deviation along direction a. So most prediction points see themselves as lying on the edge of the training set.
\end{exer}

\begin{proof}
    Let $z_i = a^T x_i = \frac{x_0^T}{\| x_0 \|} x_i$.  Then $z_i$ is a linear combination of $N(0,1)$ random variables, and hence normal, with expectation zero and variance \[ 
        \text{Var}(z_i) = \| a^T \|^2 \text{Var}(x_i) = \text{Var}(x_i) = 1
    \] as the vector $a$ has unit length and $x_i \sim N(0, 1)$.
    
    For each target point $x_i$, the squared distance from the origin is a $\chi^2_p$ distribution with mean $p$, as required.  
\end{proof}

\begin{exer}
    \begin{enumerate}[(a)]
        \item Derive equation (2.27) in the notes.
        \item Derive equation (2.28) in the notes.
    \end{enumerate}
\end{exer}

\begin{proof}
    \begin{enumerate}[(i)]
        \item We have \begin{align*}
            EPE(x_0) &= E_{y_0 | x_0} E_{\mathcal{T}}(y_0 - \hat y_0)^2 \\
                     &= \text{Var}(y_0|x_0) + E_{\mathcal T}[\hat y_0 - E_{\mathcal T} \hat y_0]^2 + [E_{\mathcal T} - x_0^T \beta]^2 \\
                     &= \text{Var}(y_0 | x_0) + \text{Var}_\mathcal{T}(\hat y_0) + \text{Bias}^2(\hat y_0).
        \end{align*}  We now treat each term individually.  Since the estimator is unbiased, we have that the third term is zero.  Since $y_0 = x_0^T \beta + \epsilon$ with $\epsilon$ an $N(0,\sigma^2)$ random variable, we must have $\text{Var}(y_0|x_0) = \sigma^2$.  

        The middle term is more difficult.  First, note that we have \begin{align*}
            \text{Var}_{\mathcal T}(\hat y_0) &= \text{Var}_{\mathcal T}(x_0^T \hat \beta) \\
                    &= x_0^T \text{Var}_{\mathcal T}(\hat \beta) x_0 \\
                    &= E_{\mathcal T} x_0^T \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1} x_0
            \end{align*} by conditioning (3.8) on $\mathcal T$.
        \item 
    \end{enumerate}
\end{proof}

\begin{exer}
    Consider a regression problem with inputs $x_i$ and outputs $y_i$, and a parameterized model $f_\theta(x)$ to be fit with least squares.  Show that if there are observations with \emph{tied} or \emph{identical} values of $x$, then the fit can be obtained from a reduced weighted least squares problem.
\end{exer}

\begin{proof}
    This is relatively simple.  WLOG, assume that $x_1 = x_2$, and all other observations are unique.  Then our RSS function in the general least-squares estimation is \[
        RSS(\theta) = \sum_{i=1}^N \left(y_i - f_\theta(x_i) \right)^2 = \sum_{i=2}^N w_i \left(y_i - f_\theta(x_i) \right)^2 
    \] where \[
        w_i = \begin{cases}
            2 & i = 2 \\
            1 & \text{otherwise}
        \end{cases}
    \]
    Thus we have converted our least squares estimation into a reduced weighted least squares estimation.  This minimal example can be easily generalised.
\end{proof}

\begin{exer}
    Suppose that we have a sample of $N$ pairs $x_i, y_i$, drawn IID from the distribution such that $x_i \sim h(x), y_i = f(x_i) + \epsilon_i, E(\epsilon_i) = 0, \text{Var}(\epsilon_i) = \sigma^2$.
    
    We construct an estimator for $f$ linear in the $y_i$, \[
        \hat f(x_0) = \sum_{i=1}^N \ell_i(x_0; \mathcal X) y_i
    \] where the weights $\ell_i(x_0; X)$ do not depend on the $y_i$, but do depend on the training sequence $x_i$ denoted by $\mathcal X$.  
    \begin{enumerate}[(a)]
        \item Show that the linear regression and $k$-nearest-neighbour regression are members of this class of estimators.  Describe explicitly the weights $\ell_i(x_0; \mathcal X)$ in each of these cases.
    \end{enumerate}
\end{exer}

\begin{proof}
    \begin{enumerate}[(a)]
        \item Recall that the estimator for $f$ in the linear regression case is given by \[
            \hat f(x_0) = x_0^T \beta 
        \] where $\beta = (X^T X)^{-1} X^T y$.  Then we can simply write \[
            \hat f(x_0) = \sum_{i=1}^N \left( x_0^T (X^T X)^{-1} X^T \right)_i y_i.
        \]  Hence \[
            \ell_i(x_0; \mathcal X) = \left( x_0^T (X^T X)^{-1} X^T \right)_i.
        \]
        
        In the $k$-nearest-neighbour representation, we have \[
            \hat f(x_0) = \sum_{i=1}^N \frac{y_i}{k} \mathbf{1}_{x_i \in N_k(x_0)}
        \] where $N_k(x_0)$ represents the set of $k$-nearest-neighbours of $x_0$.  Clearly, \[
            \ell_i(x_0; \mathcal X) = \frac{1}{k} \mathbf{1}_{x_i \in N_k(x_0)}
        \]
    \end{enumerate}
\end{proof}
\end{document}
"""
import re
from collections import defaultdict
 
main_re = re.compile(r"""\\begin{document}
                            (?P<main>.*)
                            \\end{document}""", 
                            flags=re.DOTALL + re.VERBOSE)

block_re = re.compile(r"""\\begin{(?P<block_name>exer|proof|thm|lem|prop)} # block name
                            (?P<block_contents>.*?) # Non-greedy block contents
                            \\end{(?P=block_name)}""", # closing block
                            flags=re.DOTALL + re.VERBOSE)

lists_re = re.compile(r"""\\begin{(?P<block_name>enumerate|itemize)} # list name
                            \[\(.\)\]? # Optional enumerate settings i.e. (a)
                            (?P<block_contents>.*?) # Non-greedy list contents
                            \\end{(?P=block_name)}""", # closing list
                            flags=re.DOTALL + re.VERBOSE)

header_re = re.compile(r"""\\(?P<header_name>chapter|section|subsection)
                            {(?P<header_contents>.*?)}""", #
                            flags=re.DOTALL + re.VERBOSE)

block_counter = defaultdict(lambda: 1)

block_configuration = {
    'exer': {
        "markdown_heading": "####",
        "pretty_name": "Exercise",
        "line_indent_char": "> ",
        "show_count": True
    },
    'thm': {
        "markdown_heading": "####",
        "pretty_name": "Theorem",
        "line_indent_char": "> ",
        "show_count": True
    },    
    'proof': {
        "markdown_heading": "####",
        "pretty_name": "Proof",
        "line_indent_char": "",
        "show_count": False
    },
    'enumerate': {
        "list_heading": "1.",
        "markdown_heading": "",
        "pretty_name": "",
        "line_indent_char": "",
        "show_count": False
    },
    'itemize': {
        "list_heading": "*",
        "markdown_heading": "",
        "pretty_name": "",
        "line_indent_char": "",
        "show_count": False
    },
    'section': {
        "markdown_heading": "###",
        "pretty_name": "",
        "show_count": True
    }
}

def replace_header(matchobj):
    header_name = matchobj.group('header_name')
    header_contents = matchobj.group('header_contents')
    
    header = format_block_name(header_name)
    return "{header} - {title}\n".format(header=header, title=header_contents)

def replace_block(matchobj):
    block_name = matchobj.group('block_name')
    block_contents = matchobj.group('block_contents')
    
    if block_name in {"itemize", "enumerate"}:
        formatted_contents = format_list_contents(block_name, 
                                                    block_contents)
    else:
        formatted_contents = format_block_contents(block_name,
                                                    block_contents)
    
    header = format_block_name(block_name)
    
    output_str = "{header}\n\n{block_contents}".format(
                    header=header, 
                    block_contents=formatted_contents)    
    return output_str


def format_block_contents(block_name, block_contents):
    line_indent_char = block_configuration[block_name]["line_indent_char"]
    
    output_str = ""
    for line in block_contents.lstrip().rstrip().split("\n"):
        line = line.lstrip().rstrip() 
        indented_line = line_indent_char + line + "\n"
        output_str += indented_line   
    return output_str

def format_list_contents(block_name, block_contents):
    list_heading = block_configuration[block_name]["list_heading"]
    
    output_str = ""
    for line in block_contents.lstrip().rstrip().split("\n"):
        line = line.lstrip().rstrip() 
        markdown_list_line = line.replace(r"\item", list_heading)
        output_str += markdown_list_line + "\n"
    return output_str
    
def format_block_name(block_name):
    pretty_name = block_configuration[block_name]["pretty_name"]
    show_count = block_configuration[block_name]["show_count"]
    markdown_heading = block_configuration[block_name]["markdown_heading"]
    
    block_count = block_counter[block_name] if show_count else ""
    
    block_counter[block_name] += 1
    
    output_str = "{markdown_heading} {pretty_name} {block_count}".format(
                    markdown_heading=markdown_heading, 
                    pretty_name=pretty_name, 
                    block_count=block_count)
    
    return output_str.lstrip().rstrip()
def latex_to_markdown(latex_string):
    # Get main content, skipping preamble and closing tags.
    output = main_re.search(latex_string).group("main")
    
    # Reformat, lists, blocks, and headers.
    output = lists_re.sub(replace_block, output)
    output = block_re.sub(replace_block, output)
    output = header_re.sub(replace_header, output)
    
    # Fix \\ formatting for line breaks in align blocks  
    output = re.sub(r" \\\\", r" \\\\\\\\", output)
    # Fix Align* block formatting
    output = re.sub(r"align\*", r"align", output)
    # Fix emph{} formatting
    output = re.sub(r"\\emph{(.*?)}", r"*\1*", output)
    # Fix \% formatting
    output = re.sub(r"\\%", r"%", output)
    # Fix argmax, etc.
    output = re.sub(r"\\arg(max|min)", r"\\text{arg\1}", output)
    return output

print latex_to_markdown(test)