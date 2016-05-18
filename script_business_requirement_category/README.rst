.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================================================
Script to migrate category information for  BR module
=====================================================

This script is for run once time to migrate the information from "project.category" that now is related to  business requirement on the visible field "Tags". We should use the relation with the model "business.requirement.category".

The script create the same information for the new related field "business_requirement_categ_id".


Configuration
=============

The administrator who executes this script need to set these variables to the corresponding environment:

* server
* db
* user
* password

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/xie8899/project/tree/gap_analysis_8.0.2/script_business_requirement_category/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback.


Contributors
------------

* Victor M. Martin <victor.martin@elico-corp.com>

Maintainer
----------

.. image:: https://www.elico-corp.com/logo.png
   :alt: Elico Corp
   :target: https://www.elico-corp.com

This module is maintained by Elico Corporation.

Elico Corporation offers consulting services to implement open source management software in SMEs, with a strong involvement in quality of service.

Our headquarters are located in Shanghai with branches in Hong Kong, ShenZhen and Singapore servicing customers from Greater China, Asia Pacific, Europe, Americas, etc..
