#!/usr/bin/env python

import argparse
import os.path
import yaml


def merge_configs(source_filename, target_filename):
    # TODO handle errors / test

    with open(source_filename, 'r') as f:
        source = yaml.load(f.read())
    with open(target_filename, 'r') as f:
        target = yaml.load(f.read())

    # TODO avoid overwriting existing configuration
    # TODO validate the existing configuration

    cluster_id, _ = os.path.splitext(os.path.basename(source_filename))

    # Add cluster
    cluster = source['clusters'][0]
    # The name will default to 'kubernetes'.  Set it to the cluster id
    # to provide a better guarantee of uniqueness
    cluster['name'] = cluster_id
    target['clusters'].append(cluster)

    # Add context
    context = {
        'name': cluster_id,
        'context': {
            'cluster': cluster_id,
            'user': cluster_id,
        },
    }
    target['contexts'].append(context)

    # Add user
    # TODO ensure this is the admin user
    user = source['users'][0]
    user['name'] = cluster_id
    target['users'].append(user)

    # TODO ensure atomic write
    with open(target_filename, 'w') as f:
        yaml.dump(target, f, default_flow_style=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source_config', help='Filename of config to merge from')
    default_config = '%s/.kube/config' % os.path.expanduser('~')
    parser.add_argument('--target-config', help='Filename of config to merge into',
                        default=default_config)
    args = parser.parse_args()
    merge_configs(args.source_config, args.target_config)
