
# Introduction to BIDS Apps
Franz Liem (franziskus.liem@uzh.ch)

## Description
[BIDS Apps](http://bids-apps.neuroimaging.io) are portable neuroimaging
pipelines that understand [BIDS datasets](http://bids.neuroimaging.io).
They facilitate executing standard neuroimaging pipelines,
like FreeSurfer, fmriprep, cpac, mriqc..., for processing structural and
functional MRI data.
BIDS Apps run on all three major operating systems with no need for a
complex setup and configuration and very little user input.


For more background see [Gorgolewski et al. (2017)](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005209).

For a list of available BIDS Apps see
[here](http://bids-apps.neuroimaging.io/apps/).


## What to expect
After a brief introduction to BIDS Apps and [Docker](http://docker.com)
software containers, participants will run the
[MRIQC](http://mriqc.readthedocs.io/en/latest/)
software on their laptops, to judge the quality of MRI data.

## Prerequisites
The tutorial is open to everyone with basic experience with MRI data.
No prior experience with command line tools, docker, BIDS Apps or
MRIQC is required.

## What to bring
* Laptop with Docker installed
(see guides for
[mac](https://docs.docker.com/docker-for-mac/install/),
[windows](https://docs.docker.com/docker-for-windows/install/),
[linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/))
* if possible, already download (pull) the docker container we will be
using:
    * open a terminal window/command line
    * paste the following command: `docker pull poldracklab/mriqc:0.10.4`
    * press enter and wait for the download to be finished
* download the following [BIDS-formatted](http://bids.neuroimaging.io)
example data set **#TODO**
*  optionally, bring your own BIDS-formatted MRI data
(T1w and/or functional), for instance, the result of the
**Introduction to BIDS** tutorial)

## Slides
will be posted [here](https://github.com/fliem/bids_apps_intro).

####

# Introduction to Tractography
Alessandro Crimi (alessandro.crimi@usz.ch)

## Description
Tractography is a 3D modeling technique used to visually represent neural
tracts using data collected by diffusion-weighted images (DWI).
It uses special techniques of magnetic resonance imaging (MRI) and
computer-based image analysis.

Tractography can be achieved by using available tools or by using
Python scripts. We will focus on this latter approach and on
manipulation
of the results via an opensource tool called Trackvis.

For more details I recommend the
[PhD thesis of Prof. Descoteaux](https://tel.archives-ouvertes.fr/tel-00457458/document).

## What to expect
After a brief introduction on diffusion tensor imaging, participants
will run and personalize a given Python script o their laptops to
generate a tractography.

They will learn basic use of Trackvis to analyze the results.

## Prerequisites
The tutorial is open to everyone with basic experience with MRI data,
neuroanatomy and programming. No prior experience with programming
required though a basic knowledge or willingness to learn-by-doing is
required.

## What to bring

* Laptop with Python installed (or either Linux or Conda
ready to install Python).
* [Jupiter notebook](http://jupyter.org/install)
* if possible, already
[installed the dipy library](http://nipy.org/dipy/installation.html)
(generally simply pip install dipy`)
* Download and get the license file of [Trackvis](http://trackvis.org/)

## Slides
will be posted
[here](https://github.com/alecrimi/DTItutorial/blob/master/Tutorial.pdf)
