;;; helm-bibtex.el ---

;; Copyright (C) 2013  KentaroTAKAGI <kentaro0910@gmail.com>

;; Author: KentaroTAKAGI <kentaro0910@gmail.com>
;; Keywords: bib

;; This program is free software, you can redistribute it and/or
;; modify it under the terms of the new-style BSD license.

;; You should have received a copy of the BSD license along with this
;; program. If not, see <http://www.debian.org/misc/bsd.license>.

;;; Commentary:

;;; Code:


(defvar path-to-bibtex_source "~/articles/bibtex_source.py")

(setq helm-c-source-bibtex
  '((name . "bibtex")
    (candidates . helm-bibtexkey-candidates)
    (candidate-transformer . helm-bibtexkey-candidates-transformer)
    (action . (("Insert" . insert)))))

(defun helm-bibtexkey-candidates ()
  (split-string (shell-command-to-string path-to-bibtex_source) "\n"))

(defun helm-bibtexkey-candidates-transformer (candidates)
  (mapcar 'helm-split-to-bibkey-and-description
          candidates))

(defun helm-split-to-bibkey-and-description (arg)
  (let ((re "^\\([^, ]*\\)[, ]*\\(.*\\)$")
        key
        description)
    (string-match re arg)
    (setq key (match-string 1 arg))
    (setq description (match-string 2 arg))
    (cons description key)))

(defun helm-bibtex ()
  (interactive)
  (helm-other-buffer '(helm-c-source-bibtex) "*helm-bibtex*"))

(provide 'helm-bibtex)
;;; helm-bibtex.el ends here
