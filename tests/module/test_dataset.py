# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import pytest
import unittest
from mock import MagicMock, patch, ANY
from importlib import import_module
module = import_module('dpsql.dataset')


class TestDataset(unittest.TestCase):

    # Helpers

    def setUp(self):

        # Mocks
        self.addCleanup(patch.stopall)
        self.service = MagicMock()
        self.project_id = 'project_id'
        self.dataset_id = 'dataset_id'

        # Create dataset
        self.dataset = module.Dataset(
                service=self.service,
                project_id=self.project_id,
                dataset_id=self.dataset_id)

    # Tests

    def test___repr__(self):

        # Assert values
        assert repr(self.dataset)

    def test_service(self):

        # Assert values
        assert self.dataset.service == self.service

    def test_project_id(self):

        # Assert values
        assert self.dataset.project_id == self.project_id

    def test_dataset_id(self):

        # Assert values
        assert self.dataset.dataset_id == self.dataset_id

    def test_is_existent_true(self):

        # Assert values
        assert self.dataset.is_existent

    def test_is_existent_false(self):

        # Mocks
        error = Exception()
        error.resp = MagicMock(status=404)
        patch.object(module, 'HttpError', Exception).start()
        self.service.tables.side_effect = error

        # Assert values
        assert not self.dataset.is_existent

    def test_is_existent_raise(self):

        # Mocks
        error = Exception()
        error.resp = MagicMock(status=500)
        patch.object(module, 'HttpError', Exception).start()
        self.service.tables.side_effect = error

        # Assert exception
        with pytest.raises(module.HttpError):
           self.dataset.is_existent

    def test_create_existent(self):

        # Assert exception
        with pytest.raises(RuntimeError):
           self.dataset.create()

    def test_create(self):

        # Mocks
        patch.object(self.dataset.__class__, 'is_existent', False).start()

        # Method call
        self.dataset.create()

        # Assert calls
        # TODO: add body check
        self.service.datasets.return_value.insert.assert_called_with(
                projectId=self.project_id,
                body=ANY)

    def test_delete_non_existent(self):

        # Mocks
        patch.object(self.dataset.__class__, 'is_existent', False).start()

        # Assert exception
        with pytest.raises(RuntimeError):
           self.dataset.delete()

    def test_delete(self):

        # Method call
        self.dataset.delete()

        # Assert calls
        self.service.datasets.return_value.delete.assert_called_with(
                projectId=self.project_id,
                datasetId=self.dataset_id,
                deleteContents=True)

    def test_get_tables(self):

        # Mocks
        Table = patch.object(module.jtsbq, 'Table').start()
        tables = self.service.tables.return_value
        tables.list.return_value.execute.return_value = {
            'tables': [
                {'tableReference': {'tableId': 'name'}}
            ]
        }

        # Method call
        result = self.dataset.get_tables()
        result_plain = self.dataset.get_tables(plain=True)

        # Asssert values
        result = [Table.return_value]
        result_plain == ['name']

        # Assert calls
        tables.list.assert_called_with(
            projectId=self.project_id,
            datasetId=self.dataset_id)
        Table.assert_called_with(
            service=self.service,
            project_id=self.project_id,
            dataset_id=self.dataset_id,
            table_id='name')
